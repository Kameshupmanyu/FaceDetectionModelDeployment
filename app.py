from flask import Flask , render_template , request ,redirect ,flash ,url_for
import urllib.request
import os
import cv2,numpy
from werkzeug.utils import secure_filename
face_classifier=cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def kam():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            img=cv2.imread('static/uploads/'+filename);
            #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            faces=face_classifier.detectMultiScale(img)
    
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                
                label="FaceDetected"
                label_position = (x,y)
                cv2.putText(img,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            
            cv2.namedWindow('image',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('image', 600,600)
            cv2.imshow('image',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
     
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
    return render_template('index.html', filename=filename)
    #model.DetectFace()
    #return redirect('/') 


if __name__ == "__main__":
    app.run(debug=True)
