import math as m
import matplotlib.pyplot as plt

def algorithm_DE(a, b):
    return m.sqrt(a**2+b**2)

desl_l = []
desl_r = []

time_l = []
time_r = []

pos = open("teste_horizontal.txt", 'r')
#arquivo = open("movs/teste_slide_xy.txt", 'w')
lista = pos.read().split('\n')

for i in lista:
    sublista = i.split(' ')
    if(sublista[0] == 'E'):
        desl_l.append(float(sublista[4]))
        time_l.append(float(sublista[3]))
    elif(sublista[0] == 'D'):
        desl_r.append(float(sublista[4]))
        time_r.append(float(sublista[3]))

#plt.xticks(rotation=90)
#plt.plot(time_l, desl_l, "b")
plt.plot(time_r, desl_r, "r")

plt.title("TESTE DO PONTO NA HORIZONTAL")
plt.ylabel("DESLOCAMENTO DO OLHO")
plt.xlabel("TEMPO")

plt.grid(True)

plt.show()
#arquivo.close()