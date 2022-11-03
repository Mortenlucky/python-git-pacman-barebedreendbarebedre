import random
import pygame as pg

class PacMan:
    # Constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.images = []
        for i in range(6):
            img = pg.image.load(f"images/pacman_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)
        #print("Hewwo fwom init owo",x,y)

    def move(self,new_direction):
        if new_direction == "right":
            self.x += 5
        elif new_direction == "left":
            self.x -= 5
        elif new_direction == "down":
            self.y += 5
        elif new_direction == "up":
            self.y -= 5

    def draw(self,screen,direction,tick):
        r = int((tick/2)%6)
        if direction == "left":
            screen.blit(self.images[r], (self.x, self.y))
        elif direction == "right":
            screen.blit(pg.transform.rotate(self.images[r],180), (self.x, self.y))
        elif direction == "up":
            screen.blit(pg.transform.rotate(self.images[r],-90), (self.x, self.y))
        elif direction == "down":
            screen.blit(pg.transform.rotate(self.images[r],90), (self.x, self.y))
        else:
            screen.blit(self.images[0], (self.x, self.y))