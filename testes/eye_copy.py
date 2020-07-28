import cv2
import blob
import cutEye as ce
import dot
#import numpy as np
#import cutImg
#import getCircle
#import pathFile as path

def main(isToCut):
    title_window = ''

    def on_trackbar(val):
        alpha = val / alpha_slider_max
        beta = (1.0 - alpha)
        dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
        cv2.imshow(title_window, dst)

    def nothing(x):
        pass


    #Argumentos do método 'face_cascade.detectMultiScale'(OBS.: está bom para uma curta distância)
#    scaleFactor = 1.06
 #   minNeighbors = 50
    scaleFactor = 1.3
    minNeighbors = 5

    name = "Hey dboa man?"
    #name1 = "ihoi"
    #folder = "new_imgs"
    #bar = ["right eye:", "left eye:"]
    bar_name = "value of trackbar eye:"
    #count = 0
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FPS, 30)

    limite = 0

    #importa o classificador de face
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    #importa o classificador de olho
    eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

    #Iniciando o algoritmo Blob
    blob_parm = cv2.SimpleBlobDetector_Params()
    blob_parm.filterByArea = True
    blob_parm.maxArea = 1500 #unidade em pixels
    blob_dt = cv2.SimpleBlobDetector_create(blob_parm)

    #Desenha as barras deslizantes na janela

    cv2.namedWindow(name)
    cv2.createTrackbar(bar_name, name, 0, 255, nothing)

    #Criando o ponto

    obj = dot.Dot()

    while(True):
        ret, frame = cam.read()
        #'''
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #aplica o algoritmo de detecção facial
        faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
                
        #Direito
        
        #Esquerdo
        #cv2.createTrackbar(bar[1], name, 0, 255, nothing)

        if cv2.waitKey(1) == ord('o'):
            for i in range(10):
                obj.move_dot()
         #letra 'q'
        if cv2.waitKey(1) == ord('q'):
            obj.exit_window()
            break

        for (x,y,w,h) in faces:
    
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            cv2.GaussianBlur(roi_gray, (3, 3), 0.005 * (w*h))

            #aplica o algoritmo de detecção do olho
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for i in range(len(eyes)):    
                (ex,ey,ew,eh) = eyes[i]
                if ey < 1/2*(y+h) - 100:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)   
                    try:
                        limite = cv2.getTrackbarPos(bar_name, name) 
                    except IndexError:
                        print("Há mais de um elemento na cena que está atrapalhando a detecção do usuário. Try Again Pls :)")

                    eye_img = roi_color[ey:ey+eh, ex:ex+ew]
                    if isToCut:
                        eye_img = ce.cut_eyebrows(eye_img)
                    #cutImg.salveSubImg(0, 0, np.size(eye_img, 1), np.size(eye_img, 0), eye_img, count, folder)
                    keypoints = blob.blob_process(eye_img, blob_dt, limite)
                    cv2.drawKeypoints(eye_img, keypoints, eye_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                    cv2.imshow("asdf",blob.img_blob_process(eye_img, blob_dt, limite, 1))
                    #cutImg.salveSubImg(ex, ey, ew, eh, roi_color, count)
                    #count+=1


                    #PROBLEMAS AQUI v 
                    for i in keypoints:   
                        if 30 > i.pt[0]:
                            print("left?")
                        else:
                            print("right?")
                        print(i.pt[0], end=' ')
                        print(i.pt[1])
                    
        #print(cv2.getTrackbarPos(bar_name, name) )
        #cv2.imshow(name1, u)
        cv2.imshow(name, frame)
        #print(cam.get(cv2.CAP_PROP_FPS))
    
    cam.release()
    cv2.destroyWindow(name) 
    #cv2.destroyWindow(name1) 

if __name__ == '__main__':
    print("*Olá! Eu sou um chatbot*.\nTenho apenas uma pergunta. Você está em um ambiente sem luz?[S/n]")
    print(">", end=' ')
    inp = input()
    print("\nPress the keyword 'Q' to exit or 'O' to move the dot.\n")
    if inp.upper() == 'Y':
        main(False)
    else:
        main(True)