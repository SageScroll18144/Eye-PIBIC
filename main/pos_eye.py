#posições globais 
pos_left_eye = np.array([])
pos_right_eye = np.array([])

# 0 -> LEFT AND 1 -> RIGHT 
def getAllListPos(x):
    if x == 0:
        return pos_left_eye
    else:
        return pos_right_eye

# 0 -> AXIS X AND 1 -> AXIS Y
def getLastRightPos(x):
    if x == 0:
        return pos_right_eye[len(pos_right_eye)-2]
    else:
        return pos_right_eye[len(pos_right_eye)-1]

# 0 -> AXIS X AND 1 -> AXIS Y
def getLastLefttPos(x):
    if x == 0:
        return pos_left_eye[len(pos_left_eye)-2]
    else:
        return pos_left_eye[len(pos_left_eye)-1]

def setElementInRight(x, y):
    pos_right_eye = np.append(pos_right_eye, x)
    pos_right_eye = np.append(pos_right_eye, y)

def setElementInLeft(x, y):
    pos_left_eye = np.append(pos_left_eye, x)
    pos_left_eye = np.append(pos_left_eye, y)