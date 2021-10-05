import math as m
import matplotlib.pyplot as plt

desl_l = []
desl_r = []

TEMPO = 60000

time = []

time_l = []
time_r = []

def algorithm_DE(a, b):
    return m.sqrt(a**2+b**2)

pos = open("movs/teste eye.txt", 'r')
arquivo = open("movs/teste_slide_xy.txt", 'w')
lista = pos.read().split('\n')

for i in lista:
    sublista = i.split(' ')
    x = algorithm_DE(float(sublista[1])+float(sublista[2]), float(sublista[3][:2])+float(sublista[3][2::]))
    time.append(sublista[4])
    if(sublista[0] == 'E'):
        desl_l.append(x)
        time_l.append(sublista[4])
    elif(sublista[0] == 'D'):
        desl_r.append(x)
        time_r.append(sublista[4])
    arquivo.write(str(sublista[0]) + " " + str(float(sublista[1])+float(sublista[2])) + " " + str(float(sublista[3][:2])+float(sublista[3][2::])) + " " + str(sublista[4])+"\n")
'''
passo = float(max(len(desl_l), len(desl_r))/TEMPO)

VAR = 0.0

while(TEMPO >= VAR):
    time.append(VAR)
    VAR += passo
'''

for i in range(0,TEMPO+1, 100):
    time.append(i)

'''
if(len(desl_r) < len(desl_l)):
    for i in range(len(desl_l) - len(desl_r)):
        desl_r.append(0)
elif(len(desl_r) > len(desl_l)):
    for i in range(len(desl_r) - len(desl_l)):
        desl_r.append(0)

for i in range(0, 601-570):
    desl_r.append(0)
    desl_l.append(0)

for i in range(601):
    if(desl_l[i] == 0):
        desl_l[i] = 70
    if(desl_r[i] == 0):
        desl_r[i] = 70
'''
#print(desl_l)
#plt.plot(time, [], "w")
time = list(set(time))
print(time)
#plt.plot(time_l, desl_l, "b")
#plt.plot(time_r, desl_r, "r")

plt.title("LEITURA DE UM TEXTO")
plt.ylabel("DESLOCAMENTO DO OLHO")
plt.xlabel("TEMPO")

plt.grid(True)

plt.show()
arquivo.close()