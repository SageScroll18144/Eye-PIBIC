import cv2
import blob
import cutEye as ce
import time 

def main(isToCut):
    LIM = 100
    ll = -1
    lr = -1
    tbegin = time.time()
    print("Tempo inicial: ", tbegin)
    title_window = ''

    def on_trackbar(val):
        alpha = val / alpha_slider_max
        beta = (1.0 - alpha)
        dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
        cv2.imshow(title_window, dst)

    def nothing(x):
        pass

    scaleFactor = 1.3
    minNeighbors = 5

    arquivo = open('DADOS.txt','a')

    name = "Eye tracking"
    
    bar_nameR = "value of first trackbar:"
    bar_nameL = "value of second trackbar:"
    
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
    cv2.createTrackbar(bar_nameR, name, 0, 255, nothing)
    cv2.createTrackbar(bar_nameL, name, 0, 255, nothing)

    while(True):
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)

        if cv2.waitKey(1) == ord('q'): 
            break
        elif cv2.waitKey(1) == ord('p'):
            print("VI O PONTO, tempo:", end=' ')
            print(time.time() - tbegin)

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
                        limiteR = cv2.getTrackbarPos(bar_nameR, name) 
                        limiteL = cv2.getTrackbarPos(bar_nameL, name) 
                    except IndexError:
                        print("Há mais de um elemento na cena que está atrapalhando a detecção do usuário. Try Again Pls :)")

                    eye_img = roi_color[ey:ey+eh, ex:ex+ew]
                    if isToCut:
                        eye_img = ce.cut_eyebrows(eye_img)

                    keypoints = blob.blob_process(eye_img, blob_dt, limiteR)
                    keypoints1 = blob.blob_process(eye_img, blob_dt, limiteL)
                    cv2.drawKeypoints(eye_img, keypoints, eye_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                    cv2.drawKeypoints(eye_img, keypoints1, eye_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                    #cv2.imshow("asdf",blob.img_blob_process(eye_img, blob_dt, limite, 1))
                    
                    for i in keypoints:
                        #print(ex + i.pt[0], ey + i.pt[1])
                        sd=''
                        if LIM < ex:
                            print("E ", end='')
                            sd='E'
                            ll = ex
                        elif LIM > ex:
                            print("D ", end='')
                            sd='D'
                            lr = ex
                        if ll!=-1 and lr!=-1:
                            LIM = (lr+ll)/2
                                                    
                        print(ex + i.pt[0], ey + i.pt[1], end=' ')
                        arquivo.write(sd+" "+str(ex) + " " + str(i.pt[0])+ " " +str(ey) + str(i.pt[1]) + " "+ str(time.time() - tbegin)+"\n")
                        print(time.time() - tbegin)
        
                    for i in keypoints1:
                        #print(ex + i.pt[0], ey + i.pt[1])
                        sd=''
                        if LIM < ex:
                            print("E ", end='')
                            sd='E'
                            ll = ex
                        elif LIM > ex:
                            print("D ", end='')
                            sd='D'
                            lr = ex
                        if ll!=-1 and lr!=-1:
                            LIM = (lr+ll)/2
                                                    
                        print(ex + i.pt[0], ey + i.pt[1], end=' ')
                        arquivo.write(sd+" "+str(ex+i.pt[0])+ " " +str(ey+i.pt[1]) + " "+ str(time.time() - tbegin)+"\n")
                        print(time.time() - tbegin)
                        
        cv2.imshow(name, frame)
    arquivo.close()
    cam.release()
    cv2.destroyWindow(name) 

if __name__ == '__main__':
    print("*Olá! Eu sou um chatbot*.\nTenho apenas uma pergunta. Você está em um ambiente sem luz?[S/n]")
    print(">", end=' ')
    inp = input()
    print("\nPress the keyword 'Q' to exit or 'P' to print the time.\n")
    if inp.upper() == 'S':
        main(False)
    else:
        main(True)