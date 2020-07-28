import numpy as np

class Position:
    def __init__(self):
        #posições globais 
        self.pos_left_eyeX = np.array([])
        self.pos_left_eyeY = np.array([])
        self.pos_right_eyeX = np.array([])
        self.pos_right_eyeY = np.array([])
    '''
    # 0 -> LEFT AND 1 -> RIGHT 
    def getAllListPos(self, x):
        if x == 0:
            return self.pos_left_eye
        else:
            return self.pos_right_eye
    '''
    def getLastRightPosX(self):
        if len(self.pos_right_eyeX) > 0:
            return self.pos_right_eyeY[len(self.pos_right_eyeX)-1]
        else:
            return -1
    def getLastRightPosY(self):
        if len(self.pos_right_eyeY) > 0:
            return self.pos_right_eyeY[len(self.pos_right_eyeY)-1]
        else:
            return -1

    def getLastLeftPosX(self):
        if len(self.pos_left_eyeX) > 0:
            return self.pos_left_eyeX[len(self.pos_left_eyeX)-1]
        else:
            return -1
  
    def getLastLeftPosY(self):
        if len(self.pos_left_eyeY) > 0:
            return self.pos_left_eyeY[len(self.pos_left_eyeY)-1]
        else:
            return -1

    def setElementInRight(self, x, y):
        self.pos_right_eyeX = np.append(self.pos_right_eyeX, x)
        self.pos_right_eyeY = np.append(self.pos_right_eyeY, y)

    def setElementInLeft(self, x, y):
        self.pos_left_eyeX = np.append(self.pos_left_eyeX, x)
        self.pos_left_eyeY = np.append(self.pos_left_eyeY, y)

    def putCoordinate(self, x, y):
        faceLength = 85
        if(len(self.pos_left_eyeX) > 1 and len(self.pos_right_eyeX) > 1):
            faceLength = int((int(self.getLastRightPosX()) + int(self.getLastLeftPosX())) / 2)
        
        if(x < faceLength):
            self.setElementInRight(x, y)
        else:
            self.setElementInLeft(x, y)