import cv2
import pathFile as path
import getCircle as getc
import lut
import numpy as np
import mahotas 

PATH = "ROI_261.png"
img = cv2.imread(path.path('imgs_eyes')+'/'+PATH)

img = lut.adjust_gamma(img,5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  


suave = cv2.GaussianBlur(gray, (7, 7), 0)
suave = cv2.medianBlur(suave, 7)


#OTSU
'''
T = mahotas.thresholding.rc(suave)
temp = img.copy()
temp[temp > T] = 255
temp[temp < 255] = 0
temp = cv2.bitwise_not(temp)

#ADAPTIVE THRESHOLD

''' 
bi = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 27, -4)#27, -4
bi = cv2.medianBlur(bi, 3)
bi = cv2.GaussianBlur(bi, (3, 3), 0)
#bi = cv2.medianBlur(bi, 3)
'''

#cor = lut.putAColor(suave)
#cor = cv2.applyColorMap(bi, cv2.COLORMAP_JET)
#_, bi = cv2.threshold(suave,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
##bordas = cv2.Canny(limites,0,0)
#suave = cv2.medianBlur(suave, 7)
#suave = cv2.Smooth(gray,gray,cv2.CV_GAUSSIAN,9,9)

#T, bi = cv2.threshold(suave, 80, 255, cv2.THRESH_BINARY)
#imgc = cv2.Canny(suave,suave,255/3,255, 70)
#imgBi = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 5)
#gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,3.5)
#circles = getc.circle(img, 1, 70, 30, 100,0,0)

pixels = np.array([])
media = 0
for i in range(suave.shape[0]):
    for j in range(suave.shape[1]):
        pixels = np.append(pixels, suave[i, j])
pixels = np.sort(pixels)
for i in range(len(pixels)):
    media+=pixels[i]
    print(pixels[i], end=' ')
print()
print(media/len(pixels))
print()

canny = cv2.Canny(temp,0,0)
circles = getc.circle(canny, 2, 10, 32, 200,0,0,False)
#circles = cv2.HoughCircles(suave, cv2.HOUGH_GRADIENT, 1.2,100)
#imgc = cv2.Canny(imgBi, 70, 1)
if circles is not None:
    for x, y, r in circles[0]:
       cv2.circle(img,(x,y),r,(0,255,0),2) 
       cv2.circle(img,(x,y),2,(0,0,255),3) 
 
'''
canny = cv2.Canny(bi,0,0)



circles = getc.circle(canny, 6, 100, 1, 90,5,24,False)
#circles = cv2.HoughCircles(suave, cv2.HOUGH_GRADIENT, 1.2,100)
#imgc = cv2.Canny(imgBi, 70, 1)
if circles is not None:
    for x, y, r in circles[0]:
       cv2.circle(img,(x,y),r,(0,255,0),2) 
       cv2.circle(img,(x,y),2,(0,0,255),3) 



cv2.imshow("man", suave)
cv2.imshow("pupil man", bi)
cv2.imshow("ma", canny)
cv2.imshow("canny", img)
#cv2.imshow("binary", imgBi)
cv2.waitKey(0)
cv2.destroyAllWindows()

