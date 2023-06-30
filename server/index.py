from flask import Flask, request, send_file
from flask_cors import CORS
import subprocess
from multiprocessing import Process
import uuid
import os

def process_image(img_input, output):
    print('Processing image...')
    subprocess.run(['backgroundremover', '-i', img_input, '-o', output])
    print('Image Created')
    f = open(f"ready_{output}", "w")
    f.close()

app = Flask(__name__)
CORS(app, origins=['https://wrainf.github.io/bg-remover-frontend/'])
@app.route("/upload", methods=['POST'])
def upload_image():
    print(request.files)
    filename = f"{uuid.uuid4()}.png"
    if 'file' in request.files:
        image = request.files['file']
        image.save(filename)
    else:
        return jsonify({}), 500
    img_input = filename
    outid = uuid.uuid4()
    output = f"ready_{outid}.png"
    print(output)
    data = {'id':outid }
    p = Process(target=process_image, args=(img_input, output,))
    p.start()
    return data

@app.route("/fetch/<id>", methods=['GET'])
def fetch_image(id):
    folder = os.listdir()
    for file in folder:
        if file == f"ready_{id}":
            return send_file(id, mimetype='image/png')
    return {}, 404
