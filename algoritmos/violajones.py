import numpy as np
import cv2

#importa o classificador de face
face_cascade = cv2.CascadeClassifier('/home/felipe/haarcascades/haarcascade_frontalface_default.xml')

#importa o classificador de olho
eye_cascade = cv2.CascadeClassifier('/home/felipe/haarcascades/haarcascade_eye.xml')

img = cv2.imread('/home/felipe/Downloads/h.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#aplica o algoritmo de detecção facial
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     roi_gray = gray[y:y+h, x:x+w]
     roi_color = img[y:y+h, x:x+w]

    #aplica o algoritmo de detecção facial
     eyes = eye_cascade.detectMultiScale(roi_gray)
     for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
