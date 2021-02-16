import matplotlib.pyplot as plt

desl = []

pos = open("movs/desl.txt", 'r')

for i in pos.read().split('\n'):
    desl.append(float(i))

plt.plot(desl)
plt.show()