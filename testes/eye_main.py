import cv2
import getCircle
import pathFile as path
import cutImg
import blob
import cutEye as ce
import numpy as np

def nothing(x):
  pass

''' ATUALIZAR.:
    *Distância da webcam no Lab de Física.: Tela->Mesa: 43cm; Tela->Olhos: 30cm
'''

#Argumentos do método 'face_cascade.detectMultiScale'(OBS.: está bom para uma curta distância)
scaleFactor = 1.06
minNeighbors = 50

name = "!Eye tracking!"

bar_name_left = "value of trackbar to eye left:"
bar_name_right = "value of trackbar to eye right:"

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)

#importa o classificador de face
face_cascade = cv2.CascadeClassifier(path.path('haarcascades') + '/haarcascade_frontalface_default.xml')
#importa o classificador de olho
eye_cascade = cv2.CascadeClassifier(path.path('haarcascades') + '/haarcascade_eye.xml')

#Iniciando o algoritmo Blob
blob_parm = cv2.SimpleBlobDetector_Params()
blob_parm.filterByArea = True
blob_parm.maxArea = 1500 #unidade em pixels
blob_dt = cv2.SimpleBlobDetector_create(blob_parm)

#Desenha as barras deslizantes na janela
cv2.namedWindow(name)
#Direito
cv2.createTrackbar(bar_name_left, name, 0, 255, nothing)
#Esquerdo
cv2.createTrackbar(bar_name_right, name, 0, 255, nothing)

while(True):
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #aplica o algoritmo de detecção facial
    faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)

    for (x,y,w,h) in faces:
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        #aplica o algoritmo de detecção do olho
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for i in range(len(eyes)):    
            (ex,ey,ew,eh) = eyes[i]
            if ey < 1/2*(y+h) - 100:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)   
                try:
                    limite_esquerdo = cv2.getTrackbarPos(bar_name_left, name) 
                    limite_direito = cv2.getTrackbarPos(bar_name_right, name) 
                except IndexError:
                    print("There are more one element at the scene. Please try again!")

                eye_img = roi_color[ey:ey+eh, ex:ex+ew]
                #eye_img = ce.cut_eyebrows(eye_img)
                keypoints_l = blob.blob_process(eye_img, blob_dt, limite_esquerdo)
                cv2.drawKeypoints(eye_img, keypoints_l, eye_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                keypoints_r = blob.blob_process(eye_img, blob_dt, limite_direito)
                cv2.drawKeypoints(eye_img, keypoints_r, eye_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                print(keypoints_r, end=' ')
                print(keypoints_l)
    cv2.imshow(name, frame)
    #letra 'q'
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyWindow(name) 
