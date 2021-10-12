arq = open("point.txt", 'r')

lista = arq.read().split('\n')

mediaxl=0
mediaxr=0

mediayl=0
mediayr=0

length_e=0
length_d=0

for x in lista:
    i = x.split(" ")
    if i[0] == 'E':
        mediaxl+=float(i[1])
        mediayl+=float(i[2])
        length_e+=1
    else:
        mediaxr+=float(i[1])
        mediayr+=float(i[2])
        length_d+=1

mediaxl=mediaxl/length_e
mediaxr=mediaxr/length_d
mediayl=mediayl/length_e
mediayr=mediayr/length_d

print(mediaxl)
print(mediayl)
print(mediaxr)
print(mediayr)