import cv2

def circle(img, dp, minDist, param_1, param_2, minR=0, maxR=0, condGray=True):
	if condGray == True:
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp, minDist, param1=param_1, param2=param_2, minRadius=minR, maxRadius=maxR)
	
	return circles
