from flask import Flask, request, jsonify
import os
from PIL import Image
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

sent_image = "images/"
app.config['saved_folder'] = sent_image

# Ensure upload folder exists
if not os.path.exists(sent_image):
    os.makedirs(sent_image)

@app.route('/uploadFile', methods=['POST'])
@cross_origin()
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Save the file to the upload folder
        file_path = os.path.join(app.config['sent_image'], filename)
        file.save(file_path)

if __name__ == '__main__':
    app.run(port=3000)