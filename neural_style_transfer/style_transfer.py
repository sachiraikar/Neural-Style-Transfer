import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms
from PIL import Image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.set_num_threads(2)

def load_image(path, size=256):
    image = Image.open(path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor()])
    return transform(image).unsqueeze(0).to(device)

def tensor_to_image(tensor):
    image = tensor.cpu().clone().squeeze(0).clamp(0, 1)
    return transforms.ToPILImage()(image)

def gram_matrix(tensor):
    b, c, h, w = tensor.size()
    features = tensor.view(c, h * w)
    G = torch.mm(features, features.t())
    return G

def get_features(image, model):
    layers = {
        '3': 'relu1_2',
        '6': 'relu2_2',
        '8': 'relu3_2',
        '10': 'relu4_2'
    }
    features = {}
    x = image
    for name, layer in model._modules.items():
        x = layer(x)
        if name in layers:
            features[layers[name]] = x
    return features

def run_style_transfer(content_path, style_path, output_path):
    content = load_image(content_path)
    style = load_image(style_path)
    target = content.clone().requires_grad_(True)

    model = models.squeezenet1_1(pretrained=True).features.to(device).eval()

    for param in model.parameters():
        param.requires_grad = False

    content_features = get_features(content, model)
    style_features = get_features(style, model)

    style_grams = {layer: gram_matrix(style_features[layer]) for layer in style_features}

    optimizer = optim.Adam([target], lr=0.01)
    steps = 20
    style_weight = 1e3
    content_weight = 1e0

    for step in range(steps):
        target_features = get_features(target, model)

        content_loss = torch.mean((target_features['relu4_2'] - content_features['relu4_2']) ** 2)

        style_loss = 0
        for layer in style_grams:
            target_gram = gram_matrix(target_features[layer])
            style_gram = style_grams[layer]
            style_loss += torch.mean((target_gram - style_gram) ** 2)

        total_loss = content_weight * content_loss + style_weight * style_loss

        optimizer.zero_grad()
        total_loss.backward(retain_graph=True)
        optimizer.step()

        print(f"Step {step+1}/{steps} | Total Loss: {total_loss.item():.2f}")

    image = tensor_to_image(target)
    image.save(output_path)
