import cv2
import pathFile as path

def salveSubImg(x, y, w, h, image, ROI_number=0, folder=''):
	
    ROI = image[y:y+h, x:x+w]
    if folder == '':
        cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
    else:
        cv2.imwrite(path.path(folder)+'ROI_{}.png'.format(ROI_number), ROI)

#Implementação.:
#cutImg.salveSubImg(ex, ey, ew, eh, image, count, folder)  obs.: criar 'count'