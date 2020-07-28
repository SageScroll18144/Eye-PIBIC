import pygame as pg
import random
import time

try:
    pg.init()
except:
    print("Deu merda")
    
#setup
width, height = 640, 480
dot = [int(width/2), int(height/2) ,10]

color_red = (255,0,0)
color_white = (255,255,255)

loop = True
count = 1

back_g = pg.display.set_mode((width, height))
back_g.fill(color_white)
pg.display.set_caption(".Dot")
#pg.draw.rect(back_g, color_red,[dot[0],dot[1], dot[2],dot[2]])
pg.display.update()

#loop
while loop:
    back_g.fill(color_white)
    pg.draw.rect(back_g, color_red,[dot[0],dot[1], dot[2],dot[2]])
    if (count%2) == 0:
        if input("Again? S/n").upper() == 'S':#Deslocamento do Ponto
            time.sleep(0.2)
            if random.randint(0,1) == 0:
                dot[0] += 300
            else:
                dot[0] -= 300
        else:
            loop = False
    elif (count%2) == 1:
        dot[0] = width/2
        if input("Begin? S/n").upper() == 'N':
            loop = False
    count += 1
    pg.display.update()
pg.quit()
