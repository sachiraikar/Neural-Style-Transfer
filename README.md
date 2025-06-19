# 🎨 Neural Style Transfer Web App

This is a Flask-based web application that applies **neural style transfer** to blend the *content* of one image with the *artistic style* of another. It uses a pre-trained **VGG19** model from PyTorch and provides a clean, dark-themed UI for easy interaction.

---

## 🖼️ Demo

Upload two images — one for content and one for style — and the app will generate a stylized output image.
---

## 🚀 Features

- Upload **Content** and **Style** images
- Live image **preview** before stylizing
- AI-based **style transfer** with SqueezeNet
- See and **download the result**
- Dark-themed, **modern UI** with circular loader
- No scroll layout – All images visible side-by-side

---

## 💡 How It Works

This app uses the **Gatys et al.** technique of neural style transfer. A pre-trained **SqueezeNet** extracts content and style features from the input images, and the output image is optimized to match content and style simultaneously.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **AI Model**: PyTorch (VGG19)
- **Frontend**: HTML, CSS, JavaScript
- **Image Handling**: `PIL`, `torchvision`, `werkzeug`

---
## 📁 Project Structure

```
neural-style-transfer/
├── app.py
├── style_transfer.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── uploads/
│   ├── output/
│   └── demo/ (optional screenshot)
```
---

## 📥 Download Output

After generating the stylized image, click the **📥 Download** button to save the final output.

---
