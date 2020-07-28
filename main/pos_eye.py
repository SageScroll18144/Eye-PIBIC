import numpy as np

#posições globais 
pos_left_eye = np.array([])
pos_right_eye = np.array([])

faceLength = 25

# 0 -> LEFT AND 1 -> RIGHT 
def getAllListPos(x):
    if x == 0:
        return pos_left_eye
    else:
        return pos_right_eye

def getLastRightPos():
    return pos_right_eye[len(pos_right_eye)-1]

def getLastLefttPos():
    return pos_left_eye[len(pos_left_eye)-1]

def setElementInRight(x):
    pos_right_eye = np.append(pos_right_eye, x)

def setElementInLeft(x):
    pos_left_eye = np.append(pos_left_eye, x)

def putCoordinate(x):
    if(len(pos_left_eye) > 1 and len(pos_right_eye) > 1):
        faceLength = (getLastRightPos() + getLastLefttPos()) / 2
    
    if(x < faceLength):
        setElementInRight(x)
    else:
        setElementInLeft(x)