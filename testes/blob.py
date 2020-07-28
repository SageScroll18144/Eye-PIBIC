import cv2
import cutImg
import numpy as np

def blob_process(img, detector, threshold): 
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)

    img = cv2.erode(img, None, iterations=2) 
    img = cv2.dilate(img, None, iterations=4) 
    img = cv2.medianBlur(img, 5)
    
    kp = detector.detect(img)

    return kp

def img_blob_process(img, detector, threshold, count): 
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)

    img = cv2.erode(img, None, iterations=2) 
    img = cv2.dilate(img, None, iterations=4) 
    img = cv2.medianBlur(img, 5)
    
    return img
    #cutImg.salveSubImg(0, 0, np.size(img, 1), np.size(img, 0), img, count)
