from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from style_transfer import run_style_transfer

app = Flask(__name__)

# Folders
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stylize', methods=['POST'])
def stylize():
    content = request.files['content']
    style = request.files['style']

    content_filename = secure_filename(content.filename)
    style_filename = secure_filename(style.filename)

    content_path = os.path.join(UPLOAD_FOLDER, content_filename)
    style_path = os.path.join(UPLOAD_FOLDER, style_filename)

    content.save(content_path)
    style.save(style_path)

    # Output image path
    output_path = os.path.join(OUTPUT_FOLDER, 'output.jpg')

    # Run style transfer
    run_style_transfer(content_path, style_path, output_path)

    return render_template(
        'index.html',
        output_image='output/output.jpg',
        content_image=f'uploads/{content_filename}',
        style_image=f'uploads/{style_filename}'
    )

@app.route('/download')
def download():
    return send_file('static/output/output.jpg', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
