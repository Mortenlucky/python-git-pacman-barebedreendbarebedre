# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg

## Sound ##
pg.mixer.pre_init(44100, 32, 2, 1024)
pg.mixer.init()
pg.mixer.music.load("pacman_banging.wav")
pg.mixer.music.play(loops=-1)

## Screen setup ##
pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man (clone)")



## Load images ##
pacman_images = []
for i in range(6):
    img = pg.image.load(f"images/pacman_{i}.png")
    img = pg.transform.scale(img, (32,32))
    pacman_images.append(img)


## Level ##
level = []
with open('level.txt', 'r') as level_file:
    for r, line in enumerate(level_file):
        row = []
        for c, char in enumerate(line):
            if char == "#":
                row.append("#")
            elif char == "p":
                y = r*32
                x = c*32
                row.append(" ")
            elif char == ".":
                row.append(".")
            else:
                row.append(" ")

        level.append(row)

num_rows = len(level)
num_cols = len(level[0])


tiles = []
for r, row in enumerate(level):
    for c, tile in enumerate(row):
        left = c*32
        top = r*32
        tiletemp = [left,top,tile]
        tiles.append(tiletemp)

for tile in tiles:
    print(tile[2])

turned = False

## Game Loop ##
direction = "left"
#olddirection = None
running = True
tick = 0
while running:


    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                olddirection = direction
                direction = "left"
                turned = True
            elif event.key == pg.K_d:
                olddirection = direction
                direction = "right"
                turned = True
            elif event.key == pg.K_w:
                olddirection = direction
                direction = "up"
                turned = True
            elif event.key == pg.K_s:
                olddirection = direction
                direction = "down"
                turned = True
            elif event.key == pg.K_m:
                if pg.mixer.music.get_busy():
                    pg.mixer.music.stop()
                else:
                    pg.mixer.music.play(loops=-1)
            elif event.key == pg.K_ESCAPE:
                running = False

    # Move
    if direction == "left":
        x = x - 5
    elif direction == "right":
        x = x + 5
    elif direction == "up":
        y = y - 5
    elif direction == "down":
        y = y + 5


    # Draw level #
    screen.fill((0,0,0))
    for r, row in enumerate(level):
        for c, tile in enumerate(row):
            left = c*32
            top = r*32
            if tile == "#":
                pg.draw.rect(screen, (20,20,220), pg.Rect(left+1, top+1, 30,30), 1)
            if tile == ".":
                pg.draw.circle(screen,(220,220,0), (left+15,top+15),5)
            
            #tiles.append(left)
            #tiles.append(top)
            
        #print(tiles)
        
        for tile in tiles:
            if tile[2] == "#":
                #if tile[0] < x and x < tile[0]+30 or tile[0] < x+32 and x+32 < tile[0]+30:
                ## Stole some code from Kristiyan <3
                if x+31 > tile[0]+2 and x < tile[0]+31:
                    #if tile[1]+1 < y and y < tile[1]+30
                    if y+31 > tile[1]+2 and y < tile[1]+31:
                        #print("test",tick)
                        if direction == "left":
                            x = x + 5
                        elif direction == "right":
                            x = x - 5
                        elif direction == "up":
                            y = y + 5
                        elif direction == "down":
                            y = y - 5
                        if turned:
                            direction = olddirection
                            print(olddirection)
                            turned = False
            else:
                if x+5 > tile[0] and x < tile[0]+5:
                    if y+5 > tile[1] and y < tile[1]+5:
                        olddirection = direction
                        turned = False



    # Draw pacman#
    r = int((tick/2)%6)
    if direction == "left":
        screen.blit(pacman_images[r], (x, y))
    elif direction == "right":
        screen.blit(pg.transform.rotate(pacman_images[r],180), (x, y))
    elif direction == "up":
        screen.blit(pg.transform.rotate(pacman_images[r],-90), (x, y))
    elif direction == "down":
        screen.blit(pg.transform.rotate(pacman_images[r],90), (x, y))
    else:
        screen.blit(pacman_images[0], (x, y))
            

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.05)
