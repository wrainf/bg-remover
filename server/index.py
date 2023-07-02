from flask import Flask, request, send_file, after_this_request
from flask_cors import CORS
import subprocess
from multiprocessing import Process
import uuid
import os

prevImage = ''

def process_image(img_input, output):
    f = open(f"{output}", "w")
    f.close()
    print('Processing image...')
    subprocess.run(['backgroundremover', '-i', img_input, '-o', output])
    removeFile(img_input)
    print('Image Created')

def removeFile(file):
    if os.path.exists(file):
        os.remove(file)
    

app = Flask(__name__)
CORS(app)
@app.route("/upload", methods=['POST'])
def upload_image():
    print(request.files)
    removeFile(prevImage)
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
        if file == f"ready_{id}.png" and os.path.getsize(file) > 0:
            prevImage = f"ready_{id}.png"
            return send_file(file, mimetype='image/png')
            
    return {}, 404
