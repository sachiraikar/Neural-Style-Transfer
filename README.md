# 🎨 Neural Style Transfer Web App

This is a Flask-based web application that applies **neural style transfer** to blend the *content* of one image with the *artistic style* of another. It uses a pre-trained **VGG19** model from PyTorch and provides a clean, dark-themed UI for easy interaction.

---

## 🖼️ Demo

Upload two images — one for content and one for style — and the app will generate a stylized output image.

![screenshot](static/demo/demo-ui.png) <!-- Replace with actual path or link when ready -->

---

## 🚀 Features

- Upload **Content** and **Style** images
- Live image **preview** before stylizing
- AI-based **style transfer** with VGG19
- See and **download the result**
- Dark-themed, **modern UI** with circular loader
- No scroll layout – All images visible side-by-side

---

## 💡 How It Works

This app uses the **Gatys et al.** technique of neural style transfer. A pre-trained **VGG19** extracts content and style features from the input images, and the output image is optimized to match content and style simultaneously.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **AI Model**: PyTorch (VGG19)
- **Frontend**: HTML, CSS, JavaScript
- **Image Handling**: `PIL`, `torchvision`, `werkzeug`

---

## 📦 Installation

```bash
git clone https://github.com/your-username/neural-style-transfer-app.git
cd neural-style-transfer-app
pip install -r requirements.txt
python app.py
````

> App will run on `http://127.0.0.1:5000/`

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

## 🧠 Sample Output

|                      Content                     |                      Style                     |                      Output                     |
| :----------------------------------------------: | :--------------------------------------------: | :---------------------------------------------: |
| <img src="static/demo/content.jpg" width="150"/> | <img src="static/demo/style.jpg" width="150"/> | <img src="static/demo/output.jpg" width="150"/> |

---

## 📥 Download Output

After generating the stylized image, click the **📥 Download** button to save the final output.

---

## 🙌 Acknowledgments

* [PyTorch VGG19 pretrained model](https://pytorch.org/vision/stable/models/generated/torchvision.models.vgg19.html)
* [Neural Style Transfer paper (Gatys et al.)](https://arxiv.org/abs/1508.06576)

---

## 📃 License

MIT License

---
