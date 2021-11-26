from flask import Flask

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask.templating import render_template
from PIL import Image

import numpy as np
import io
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


app = Flask(__name__,static_folder='static')
app.secret_key = 'super secret key'
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            siyah_beyaz_kaydet("uploads/"+filename)
            return redirect(url_for('uploaded_file',filename=filename))
        
    return render_template('index.html')

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
def siyah_beyaz_kaydet(isim: str):
    file=Image.open(isim)
    gray = file.convert('L')
    file = gray.point(lambda x: 0 if x<128 else 255, '1') 
    file.save(isim)

