import time
import random
import pygame as pg
from ghost import Ghost
from pacmanclass import PacMan


pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man (clone)")

# Creating Object
ghosts = []
for i in range(1):
    ghost = Ghost(random.randint(32,200),random.randint(32,200))
    ghosts.append(ghost)
print(ghosts)
pacman = PacMan(32,32)


direction = None
running = True
tick = 0
while running:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                #olddirection = direction
                direction = "left"
                #turned = True
            elif event.key == pg.K_d:
                #olddirection = direction
                direction = "right"
                # = True
            elif event.key == pg.K_w:
                #olddirection = direction
                direction = "up"
                #turned = True
            elif event.key == pg.K_s:
                #olddirection = direction
                direction = "down"
                #turned = True
            elif event.key == pg.K_ESCAPE:
                running = False

    # Logic
    for ghost in ghosts:
        ghost.move(tick,pacman.x,pacman.y)
    pacman.move(direction)

    # Drawraw
    screen.fill((0,0,0))
    for ghost in ghosts:
        ghost.draw(screen,tick)
    #print("pacman x: ",pacman.x)
    pacman.draw(screen,direction,tick)
    
    pg.display.flip()

    tick += 1
    #print(tick)
    time.sleep(0.05)