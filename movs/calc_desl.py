import math as m
import matplotlib.pyplot as plt

desl_l = []
desl_r = []

TEMPO = 60000

time_e = []
time_d = []

def algorithm_DE(a, b):
    return m.sqrt(a**2+b**2)

pos = open("movs/DaP2.txt", 'r')

lista = pos.read().split('\n')

for i in lista:
    sublista = i.split(' ')
    x = algorithm_DE(float(sublista[1]), float(sublista[2]))
    if(sublista[0] == 'E'):
        desl_l.append(x)
        time_e.append(sublista[3])
    elif(sublista[0] == 'D'):
        desl_r.append(x)
        time_d.append(sublista[3])
'''
passo = float(max(len(desl_l), len(desl_r))/TEMPO)

VAR = 0.0

while(TEMPO >= VAR):
    time.append(VAR)
    VAR += passo
'''
if(len(desl_r) < len(desl_l)):
    for i in range(len(desl_l) - len(desl_r)):
        desl_r.append(0)
elif(len(desl_r) > len(desl_l)):
    for i in range(len(desl_r) - len(desl_l)):
        desl_r.append(0)

for i in range(len(desl_r)):
    print(time_d[i]," " , desl_r[i])
'''
print("\nDIREITO.:")

for i in range(len(desl_r)):
    print(time[i]," " , desl_r[i])
'''