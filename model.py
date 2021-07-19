import cv2
#import numpy as np
#from deepface import DeepFace
face_classifier=cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
def DetectFace():
    cam = cv2.VideoCapture(0)

    #cv2.namedWindow("Emotion Detection")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Face Detect", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            break
            
    cam.release()
    cv2.destroyAllWindows()
    #if k%256 == 32:
     #result=DeepFace.analyze(frame,actions=['emotion'])
    #ans=result['dominant_emotion']
     #cv2.imshow(ans,img)
    faces=face_classifier.detectMultiScale(frame)
    
    for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            #label=result['dominant_emotion']
            label="FaceDetected"
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            
            cv2.imshow('Face Detector',frame)
            cv2.waitKey(0)
            #return 'THANKS FOR VISITING MY SITE...'
