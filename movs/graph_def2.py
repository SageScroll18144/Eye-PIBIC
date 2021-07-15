import math as m
import matplotlib.pyplot as plt

desl = []
time = []

def algorithm_DE(a, b):
    return m.sqrt(a**2+b**2)

pos = open("movs/olho direito.txt", 'r')

lista = pos.read().split('\n')

for i in lista:
    sublista = i.split(' ')
    #subdasub = sublista[len(sublista)-1].split('.')
    desl.append(float(sublista[len(sublista)-1]))
    time.append(float(sublista[0]))

plt.plot(time, desl, "r")
plt.plot(time, desl, "ro")
#plt.plot(time, desl_r, "rs")

plt.title("LEITURA DE UM TEXTO")
plt.ylabel("DESLOCAMENTO DO OLHO")
plt.xlabel("TEMPO(s)")
plt.xticks(rotation = 90)
plt.grid(True)

plt.show()
