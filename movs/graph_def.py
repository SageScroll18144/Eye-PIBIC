import math as m
import matplotlib.pyplot as plt

desl_l = []
desl_r = []

TEMPO = 60000

time = []

def algorithm_DE(a, b):
    return m.sqrt(a**2+b**2)

pos = open("movs/DaP.txt", 'r')

lista = pos.read().split('\n')

for i in lista:
    sublista = i.split(' ')
    x = algorithm_DE(float(sublista[1]), float(sublista[2]))
    if(sublista[0] == 'E'):
        desl_l.append(x)
    elif(sublista[0] == 'D'):
        desl_r.append(x)
'''
passo = float(max(len(desl_l), len(desl_r))/TEMPO)

VAR = 0.0

while(TEMPO >= VAR):
    time.append(VAR)
    VAR += passo
'''

for i in range(0,TEMPO+1, 100):
    time.append(i)

if(len(desl_r) < len(desl_l)):
    for i in range(len(desl_l) - len(desl_r)):
        desl_r.append(0)
elif(len(desl_r) > len(desl_l)):
    for i in range(len(desl_r) - len(desl_l)):
        desl_r.append(0)


for i in range(0, 601-570):
    desl_r.append(0)
    desl_l.append(0)
    
#plt.plot(time, [], "w")
plt.plot(time, desl_l, "b-")
plt.plot(time, desl_r, "r-")

plt.title("LEITURA DE UM TEXTO")
plt.ylabel("DESLOCAMENTO DO OLHO")
plt.xlabel("TEMPO")

plt.grid(True)

plt.show()
