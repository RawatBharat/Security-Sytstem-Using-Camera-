import cv2 
import pickle

# Loading HAAR face classifier
face_cascade = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml.txt')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

# Initialize Webcam
cap = cv2.VideoCapture(0)

count = 0
while True:
    
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)   
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        
        id_,conf = recognizer.predict(roi_gray)
        if conf>80 and conf<100:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA ) 
            count = 0
            
             
        else:
            count += 1
            #print(count)
            if count == 40:
                import alert        
                count = 0 
           
        color=(255,0,0)#BGR
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame, (x,y),(end_cord_x, end_cord_y), color, stroke)
        

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
