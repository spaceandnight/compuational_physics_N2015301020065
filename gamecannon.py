import pygame,sys
import numpy as np
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Cannon Shell(press space)")
v = 0.8
a = 45
pos_x = 0
pos_y = 398
vel_x = 0
vel_y = 0
g = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
    screen.fill((255,255,255))
    keys = pygame.key.get_pressed()
    if  keys[K_LEFT]:
        a = 30
    if  keys[K_DOWN]:
        a = 45
    if  keys[K_RIGHT]:
        a = 60
    if  keys[K_UP]:
        a = 75
    if  keys[K_SPACE]:
        pos_x = 0
        pos_y = 398
        ra = a * 3.14 / 180
        vel_x = v * np.cos(ra)
        vel_y = -v * np.sin(ra)
        g = 0.00098
    pos_x += vel_x
    pos_y += vel_y
    vel_y += g
    if pos_y > 398:
        g = 0
        vel_x = 0
        vel_y = 0
    color = 255,0,0
    width = 0
    pos = pos_x, pos_y, 8, 8
    pygame.draw.rect(screen, color, pos, width)
    pygame.display.update()