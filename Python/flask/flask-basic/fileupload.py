from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
import os

folder = 'C:\\Users\\Max Mustermann\\Documents\\Eigene Dukomente\\Examples\\Python\\flask_Example'
extensions = ['txt', 'jpg', 'jpeg', 'png']
app = Flask(__name__)

def allowed(filename):
    if filename.rsplit('.', 1)[1].lower() in extensions:
        return True
    else:
        return False

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        uploadfile = request.files['file']

        if uploadfile.filename == '':
            return redirect(request.url)
            
        if allowed(uploadfile.filename):
            filename = secure_filename(uploadfile.filename)
            uploadfile.save(os.path.join(folder, filename))
            return redirect(request.url)

    return render_template('fileuploads.html')
    
if __name__ == "__main__":
    app.run(port=1887, debug=True)

