import numpy as np

class Position:
    def __init__(self):
        #posições globais 
        self.pos_left_eye = np.array([])
        self.pos_right_eye = np.array([])

    # 0 -> LEFT AND 1 -> RIGHT 
    def getAllListPos(self, x):
        if x == 0:
            return self.pos_left_eye
        else:
            return self.pos_right_eye

    def getLastRightPos(self):
        if len(self.pos_right_eye) > 0:
            return self.pos_right_eye[len(self.pos_right_eye)-1]
        else:
            return -1

    def getLastLeftPos(self):
        if len(self.pos_left_eye) > 0:
            return self.pos_left_eye[len(self.pos_left_eye)-1]
        else:
            return -1

    def setElementInRight(self, x):
        self.pos_right_eye = np.append(self.pos_right_eye, x)

    def setElementInLeft(self, x):
        self.pos_left_eye = np.append(self.pos_left_eye, x)

    def putCoordinate(self, x):
        faceLength = 25
        if(len(self.pos_left_eye) > 1 and len(self.pos_right_eye) > 1):
            faceLength = int((int(self.getLastRightPos()) + int(self.getLastLeftPos())) / 2)
        
        if(x < faceLength):
            self.setElementInRight(x)
        else:
            self.setElementInLeft(x)
