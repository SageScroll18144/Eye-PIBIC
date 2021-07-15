pos = open("movs/DaP2.txt", 'r')

lista = pos.read().split('\n')

for i in lista:
    if(i[0] == 'E'):
        print(i)