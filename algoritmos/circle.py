import cv2
import numpy as np


def pupil(img, dp, minDist, param_1, param_2, minR, maxR):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp, minDist, param1=param_1, param2=param_2, minRadius=minR, maxRadius=maxR)
	
	return circles


PATH = '/home/felipe/Imagens/ballb.png'  

frame = cv2.imread(PATH)

#Talvez tenha que alterar os argumentos...
circles = pupil(frame, 1, 260, 30, 65, 0, 0)
if circles is not None:
    for x, y, r in circles[0]:
        cv2.circle(frame,(x,y),r,(0,255,0),2)

cv2.imshow('Xamaa',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

