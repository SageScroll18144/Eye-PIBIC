import pygame as pg
import random
import time

try:
    pg.init()
except:
    print("Ocorreu algum erro")
    
width, height = 320, 240
dot = [int(width/2), int(height/2) ,10]

color_red = (255,0,0)
color_white = (255,255,255)

back_g = pg.display.set_mode((int(2*width), int(2*height)))
back_g.fill(color_white)
pg.display.set_caption(".Dot")
dot_object = pg.Surface((width, height), pg.SRCALPHA)
pg.draw.circle(dot_object, color_red, [int(width/2), int(height/2)], 5)

def move_dot():
    lado = 0
    back_g.fill(color_white)
    back_g.blit(dot_object, [int(width/2), int(height/2)])
    pg.display.flip()
    time.sleep(0.2)
    if random.randint(0,1) == 0:
        lado = 300
    else:
        lado = -300
        
    back_g.fill(color_white)
    back_g.blit(dot_object, [int(width/2+lado), int(height/2)]) 
    pg.display.flip()
    time.sleep(0.2)
def exit_window():
    pg.quit()

'''TESTE.:
for i in range(50): 
    move_dot()
exit_window()
'''
'''
FALTA CRIAR UM MÉTODO DE INICIALIZAÇÃO

'''
