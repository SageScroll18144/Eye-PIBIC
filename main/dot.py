import pygame as pg
import random
import time
import numpy as np

class Dot:
    def __init__(self):
        try:
            pg.init()
        except:
            print("Ocorreu algum erro")
            
        self.inf_display = pg.display.Info()
        #self.width, self.height = 640, 480
        self.width, self.height = self.inf_display.current_w, self.inf_display.current_h

        self.color_red = (255,0,0)
        self.color_white = (255,255,255)

        self.back_g = pg.display.set_mode((int(self.width), int(self.height)), pg.RESIZABLE)
        self.back_g.fill(self.color_white)
        pg.display.set_caption(".Dot")
        self.dot_object = pg.Surface((self.width, self.height), pg.SRCALPHA)
        pg.draw.circle(self.dot_object, self.color_red, [int(self.width/4), int(self.height/4)], 5)

        pg.display.update()

        #Tempo de movimento do ponto
        self.timeDot = 0

        self.list_times = np.array([])

    def move_dot(self):
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                # There's some code to add back window content here.
                surface = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
        w, h = pg.display.get_surface().get_size()
        lado = 0
        self.back_g.fill(self.color_white)
        self.back_g.blit(self.dot_object, [w/4-40, h/4-40])
        pg.display.flip()

        self.timeDot = random.random()
        time.sleep(self.timeDot)
        
        self.list_times = np.append(self.list_times, self.timeDot)

        if random.randint(0,1) == 0:
            lado = 600 
        else:
            lado = -600 
            
        self.back_g.fill(self.color_white)
        self.back_g.blit(self.dot_object, [int((w/4-40)+lado), int(h/4-40)]) 
        pg.display.flip()
        time.sleep(0.2)

    def getTimeDot(self):
        return self.timeDot    
    
    def exit_window(self):
        pg.quit()

    def EventMovement(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_o:
                   return True
        return False

    def isToClose(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return True
            else:
                return False

    def getListOfTimes(self):
        return self.list_times