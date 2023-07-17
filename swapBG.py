import pygame as pg
import numpy as np
import math
import random

clock = pg.time.Clock()
FPS = 60

#You can change the screen size here
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

#Creating the game window
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Setting the title of the game window
pg.display.set_caption("Swap Game Background")
bg = pg.image.load("bg2.png").convert()
bg_width = bg.get_width()#getting the width of the background image

scroll = 0
tiles = math.ceil(SCREEN_WIDTH/bg_width) +1  #calculating the number of tiles required to fill the screen

run = True
while run:

    #Setting the FPS
    clock.tick(FPS)

    for i in range (tiles):
        screen.blit(bg, (i*bg_width+scroll,0)) #this will fill up the entire screen with repeating background

    scroll -= 5 #this will make the background move from right to left

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()

