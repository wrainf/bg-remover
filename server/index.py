from flask import Flask, request, send_file
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, origins=['https://localhost:5000'])
@app.route("/upload", methods=['POST'])
def upload_image():
    print(request.files)
    if 'file' in request.files:
        image = request.files['file']
        image.save('upload.png')
        
    imageInput = 'upload.png'
    output = 'output.png'
    subprocess.run(['backgroundremover', '-i', imageInput, '-o', output])
    return send_file("output.png", mimetype='image/png')

