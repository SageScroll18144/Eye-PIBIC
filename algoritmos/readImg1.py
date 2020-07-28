import cv2
import pathFile as path
import getCircle as getc
import lut
import numpy as np
import cutEye as ce

def blob_process(img, detector, threshold): 
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)

    img = cv2.erode(img, None, iterations=2) 
    img = cv2.dilate(img, None, iterations=4) 
    img = cv2.medianBlur(img, 5)

    kp = detector.detect(img)

    return kp


PATH = "face1.png"

img = cv2.imread(PATH)

scaleFactor = 1.05
minNeighbors = 15

#'''
img = lut.adjust_gamma(img,2)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

#suave = cv2.GaussianBlur(gray, (7, 7), 0)
#suave = cv2.medianBlur(suave, 7)
#'''

first = []
first1 = []
#importa o classificador de face
face_cascade = cv2.CascadeClassifier(path.path('haarcascades') + '/haarcascade_frontalface_default.xml')
#importa o classificador de olho
eye_cascade = cv2.CascadeClassifier(path.path('haarcascades') + '/haarcascade_eye.xml')


#Iniciando o algoritmo Blob
blob_parm = cv2.SimpleBlobDetector_Params()
blob_parm.filterByArea = True
blob_parm.maxArea = 1500 #unidade em pixels
blob_dt = cv2.SimpleBlobDetector_create(blob_parm)

#Pré-Processamento
img = cv2.medianBlur(img, 7)
#img = cv2.GaussianBlur(img, (7, 7), 0)

#ALgoritmo de Blob
limite = [120, 109] #Alterar valor de acordo com o tipo de iluminação do ambiente da imagem
count = 0
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#aplica o algoritmo de detecção facial
faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    #aplica o algoritmo de detecção do olho
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        if ey < 1/2*(y+h) - 100:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
          #cv2.circle(roi_color, (int(ex+ew/2), int(ey+eh/2)), 2, (0,0,255), 3)
          eye_img = roi_color[ey:ey+eh, ex:ex+ew]
          eye_img = ce.cut_eyebrows(eye_img)
          gray_frame = cv2.cvtColor(eye_img, cv2.COLOR_BGR2GRAY) 
          _, cimg = cv2.threshold(gray_frame, limite[count], 255, cv2.THRESH_BINARY)

          cimg = cv2.erode(cimg, None, iterations=2) 
          cimg = cv2.dilate(cimg, None, iterations=4) 
          cimg = cv2.medianBlur(cimg, 5)

          if count == 0:
            first = cimg
            first1 = eye_img
          if count > 1:
            count = 0
          keypoints = blob_process(eye_img, blob_dt, limite[count])
          cv2.drawKeypoints(eye_img, keypoints, eye_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
          count += 1
    break
cv2.imshow("man", img)
cv2.imshow("an", eye_img)
cv2.imshow("adn", cimg)
cv2.imshow("ad", first)
cv2.imshow("a", first1)
cv2.waitKey(0)
cv2.destroyAllWindows()

