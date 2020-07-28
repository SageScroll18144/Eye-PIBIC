import cv2
import getCircle
import pathFile as path
import cutImg
import blob
import cutEye as ce
import numpy as np

def nothing(x):
  pass

'''
    *Distância da webcam no Lab de Física.: Tela->Mesa: 43cm; Tela->Olhos: 30cm
'''

#Argumentos do método 'face_cascade.detectMultiScale'(OBS.: está bom para uma curta distância)
scaleFactor = 1.06
minNeighbors = 50

name = "Hey dboa man?"
#name1 = "ihoi"
#folder = "new_imgs"
bar = ["right eye:", "left eye:"]
#count = 0
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

while(True):
    ret, frame = cam.read()
    #'''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #aplica o algoritmo de detecção facial
    faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
    
    #Desenha as barras deslizantes na janela
    cv2.namedWindow(name)
    #Direito
    cv2.createTrackbar(bar[0], name, 0, 255, nothing)
    #Esquerdo
    cv2.createTrackbar(bar[1], name, 0, 255, nothing)

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
                    limite = cv2.getTrackbarPos(bar[i], name) 
                except IndexError:
                    print("Há mais de um elemento na cena que está atrapalhando a detecção do usuário. Try Again Pls :)")

                eye_img = roi_color[ey:ey+eh, ex:ex+ew]
                #eye_img = ce.cut_eyebrows(eye_img)
                #cutImg.salveSubImg(0, 0, np.size(eye_img, 1), np.size(eye_img, 0), eye_img, count, folder)
                keypoints = blob.blob_process(eye_img, blob_dt, limite)
                cv2.drawKeypoints(eye_img, keypoints, eye_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                #blob.img_blob_process(eye_img, blob_dt, limite, count)
                #cutImg.salveSubImg(ex, ey, ew, eh, roi_color, count)
                #count+=1 
    
    #cv2.imshow(name1, u)
    cv2.imshow(name, frame)
    #print(cam.get(cv2.CAP_PROP_FPS))

    #letra 'q'
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyWindow(name) 
#cv2.destroyWindow(name1) 