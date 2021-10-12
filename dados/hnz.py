import math as m

def algorithm_DE(a, b):
    return m.sqrt(a**2+b**2)

pos = open("teste_h.txt", 'r')
arquivo = open("teste_horizontal.txt", 'w')
lista = pos.read().split('\n')
#arquivo.write(sd+" "+str(ex) + " " + str(i.pt[0])+ " " +str(ey) + str(i.pt[1]) + " "+ str(time.time() - tbegin)+"\n")
for i in lista:
    #x = algorithm_DE(float(sublista[1])+float(sublista[2]), float(sublista[3][:2])+float(sublista[3][2::]))
    sublista = i.split(' ')
    if(len(sublista) == 4):
        x = algorithm_DE(float(sublista[1]), float(sublista[2]))
        arquivo.write(i + " " + str(x) + "\n")
    else:
        x = algorithm_DE(float(sublista[1])+float(sublista[2]), float(sublista[3][:2])+float(sublista[3][2::]))
        arquivo.write(str(sublista[0]) + " " + str(float(sublista[1])+float(sublista[2])) + " " + str(float(sublista[3][:2])+float(sublista[3][2::])) + " " + str(sublista[4])+" "+ str(x)+"\n")
    #arquivo.write(str(sublista[0]) + " " + str(float(sublista[1])+float(sublista[2])) + " " + str(float(sublista[3][:2])+float(sublista[3][2::])) + " " + str(sublista[4])+"\n")
