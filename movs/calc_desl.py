import math as m

def algorithm_DE(a, b):
    return m.sqrt(a**2+b**2)

pos = open("posicoes.txt", 'r')

lista = pos.read().split('\n')

for i in lista:
    sublista = i.split(' ')
    print(algorithm_DE(float(sublista[0]), float(sublista[1])))