from pathlib import Path
import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = str(Path().absolute())+'\images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tif','tiff'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def up():
   if request.method == 'POST':
         if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
         f = request.files['file']

         if f.filename == '':
            flash('No selected file')
            return redirect(request.url)

         if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(UPLOAD_FOLDER, filename))
            return render_template('upload.html')
if __name__ == '__main__':
   app.run(debug = True)