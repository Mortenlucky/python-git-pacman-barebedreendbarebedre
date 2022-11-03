import random
import pygame as pg

class Ghost:
    # Constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #print("Hewwo fwom init owo",x,y)
        self.images = []
        for i in range(2):
            img = pg.image.load(f"images/ghost_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

    def move(self,tick,pacx,pacy):
        tmove = int((tick/2)%2)
        if tmove == 0:
            
            #if self.x > pacman.x:
                #self.x -= 5
            #elif self.x < pacman.x:
                #self.x += 5
            #elif self.y > pacman.y:
                #self.y -= 5
            #elif self.y < pacman.y:
                #self.y += 5
            
            if pacx >= self.x:
                self.x += 5
                if pacy >= self.y:
                    self.y += 5
                else:
                    self.y -= 5
            else:
                self.x -= 5
                if pacy >= self.y:
                    self.y += 5
                else:
                    self.y -= 5

    def draw(self,screen,tick):
        r = int((tick/2)%2)
        screen.blit(self.images[r], (self.x, self.y))