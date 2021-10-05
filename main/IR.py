import cv2
import blob

alpha_slider_max = 255
title_window = 'Linear Blend'

def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
    cv2.imshow(title_window, dst)

def nothing(x):
    pass

img = cv2.imread('IR3.png')

cv2.namedWindow(title_window)

trackbar_name = 'Alpha x'
cv2.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, nothing)

blob_parm = cv2.SimpleBlobDetector_Params()
blob_parm.filterByArea = True
blob_parm.maxArea = 1500 #unidade em pixels
blob_dt = cv2.SimpleBlobDetector_create(blob_parm)

while(True):

    vl = cv2.getTrackbarPos(trackbar_name, title_window)

    keypoints = blob.blob_process(img, blob_dt, vl)
    cv2.drawKeypoints(img, keypoints, img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    #print(cv2.getTrackbarPos(trackbar_name, title_window))

    cv2.imshow(title_window,img)

    if cv2.waitKey(1) == ord('q'): 
        break
cv2.destroyAllWindows()