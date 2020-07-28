import cv2
import blob
import cutEye as ce
import dot
import pos

def main(isToCut):
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

    name = "Eye tracking"
    
    bar_name = "value of trackbar eye:"
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

    #Objeto das coordenadas
    Coordinate = pos.Position()

    while(True):
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
        
        obj.EventMovement()
        '''
        if cv2.waitKey(1) == ord('o'):
            #for i in range(10):
            obj.move_dot()
        '''
        if cv2.waitKey(1) == ord('q') or obj.isToClose():
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

                    keypoints = blob.blob_process(eye_img, blob_dt, limite)
                    cv2.drawKeypoints(eye_img, keypoints, eye_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                    #cv2.imshow("asdf",blob.img_blob_process(eye_img, blob_dt, limite, 1))

                    for i in keypoints:
                        for j in range(len(i.pt)):
                            Coordinate.putCoordinate(i.pt[j])
                            #print(Coordinate.getLastRightPos())
                            '''
                            if(i.pt[j] < 25):
                                print(i.pt[j], end='r ')
                            else: 
                                print(i.pt[j], end='l ')
                        print()
                        '''
                    
        cv2.imshow(name, frame)
    
    cam.release()
    cv2.destroyWindow(name) 

if __name__ == '__main__':
    print("*Olá! Eu sou um chatbot*.\nTenho apenas uma pergunta. Você está em um ambiente sem luz?[S/n]")
    print(">", end=' ')
    inp = input()
    print("\nPress the keyword 'Q' to exit or 'O' to move the dot.\n")
    if inp.upper() == 'S':
        main(False)
    else:
        main(True)