import math as m

def algorithm_DE(a, b):
    return m.sqrt(a**2+b**2)

pos = open("movs/tnormal_cam.txt", 'r')

lista = pos.read().split('\n')

for i in lista:
    if(i[0] == 'E'):
        x = i.split(" ")
        print(algorithm_DE(float(x[1]), float(x[2])), end=' ')
        print(x[3])