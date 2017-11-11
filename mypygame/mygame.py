import pygame,sys
import numpy as np
import math
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1024,600))
pygame.display.set_caption("Cannon Shell")
black = 0,0,0
white = 255,255,255
red = 255,0,0
gold = 255,215,0
myfont1 = pygame.font.Font(None,30)
myfont2 = pygame.font.Font(None,60)
myfont3 = pygame.font.Font(None,200)
textImage1 = myfont1.render("Use 'left' and 'right' to move, use 'up' and 'down' to change the angle.", True, black)
textImage2 = myfont1.render("Press 'space' to increase power and fire the shell to hit the target.", True, black)
textImage3 = myfont1.render("If you get a score of 100, you will win this game.", True, black)
textImage4 = myfont1.render("Now,let's start.", True, black)
textImage5 = myfont2.render("start", True, black)
textImage6 = myfont1.render("ammunition", True, black)
textImage7 = myfont1.render("power", True, black)
textImage8 = myfont3.render("You Win", True, black)
textImage9 = myfont3.render("Game Over", True, black)
textImagea = myfont2.render("quit", True, black)
textImageb = myfont2.render("restart", True, black)
gro1 = pygame.image.load("ground.png").convert_alpha()
tan = pygame.image.load("tan.png").convert_alpha()
gun = pygame.image.load("gun.png").convert_alpha()
vel = 0
vel_x = 0
vel_y = 0
am = 240
pw = 0
g = 0.008
tank_x = 0
tank_a = 0
i = 0
i_1 = 0
i_2 = 1
j = 0
mz1 = 0
mz2 = 0
mz3 = 0
mz4 = 0
mz5 = 0
score = 0
shell_x = 0
shell_y = 0
mouse_dx = 0
mouse_dy = 0
pygame.key.set_repeat(20)
target_x1 = random.randint(270, 994)
target_y1 = random.randint(80, 480)
target_x2 = random.randint(270, 994)
target_y2 = random.randint(80, 480)
target_x3 = random.randint(270, 994)
target_y3 = random.randint(80, 480)
target_x4 = random.randint(270, 994)
target_y4 = random.randint(80, 480)
target_x5 = random.randint(270, 994)
target_y5 = random.randint(80, 480)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                tank_x -= 5
            elif event.key == K_UP:
                tank_a += 2
            elif event.key == K_RIGHT:
                tank_x += 5
            elif event.key == K_DOWN:
                tank_a -= 2
            elif event.key == K_SPACE:
                i_1 = 1
        if event.type == KEYUP:
            if event.key == K_SPACE:
                i_1 = 0
                i_2 = 1
                j += 1
    if i_1 == 1:
        if i_2 == 1:
            pw += 0.4
        if i_2 == 0:
            pw -= 0.4
    if i_1 == 0:
        pw -= 0.8 
    if pw < 0:
        i_2 = 1
        pw = 0
    if pw > 240:
        i_2 = 0
        pw = 240
    if am > 240:
        am = 240
    if tank_x < 0:
            tank_x = 0
    if tank_x > 360:
            tank_x = 360
    if tank_a < 0:
        tank_a = 0
    if tank_a > 75:
        tank_a = 75
    vel = 0.8
    screen.fill(white)
    if i == 0:
        screen.blit(textImage1, (100,100))
        screen.blit(textImage2, (100,150))
        screen.blit(textImage3, (100,200))
        screen.blit(textImage4, (100,250))
        width = 0
        pos = 412, 350, 200, 100
        pygame.draw.rect(screen, red, pos, width)
        width = 5
        pos = 412, 350, 200, 100
        pygame.draw.rect(screen, black, pos, width)
        screen.blit(textImage5, (462,380))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_dx,mouse_dy = event.pos
                if mouse_dx <= 612 and mouse_dx >= 412 and mouse_dy <= 450 and mouse_dy >= 350:
                    i = 1
    if i == 1:
        screen.blit(textImage6, (10,10))
        screen.blit(textImage7, (420,10))
        ar = math.radians(tank_a)
        ars = np.sin(ar)
        arc = np.cos(ar)
        width = 0
        pos = 140,10,am,20
        pygame.draw.rect(screen, red, pos, width)
        pos = 500,10,pw,20
        pygame.draw.rect(screen, gold, pos, width)
        width = 3
        pos = 140, 10, 240, 20
        pygame.draw.rect(screen, black, pos, width)
        width = 3
        pos = 500, 10, 240, 20
        pygame.draw.rect(screen, black, pos, width)
        if j > 2:
            j = 2
        if j == 1:
            shell_x = int(tank_x + 60 + 68 * arc)
            shell_y = int(542 - 68 * ars)
            vel = pw / 60
            vel_x = vel * arc
            vel_y = -vel * ars
            am -= 20
            j = 2
        if j == 2:
            vel_y += g
            shell_x += vel_x
            shell_y += vel_y
            width = 0
            radius = 6
            trs_x = int(shell_x)
            trs_y = int(shell_y)
            pos = trs_x,trs_y
            pygame.draw.circle(screen, red, pos, radius, width)
        if shell_x > 1024:
            vel_x = -vel_x
        if shell_y < 0:
            vel_y = -vel_y
        if shell_x < 0 or shell_y > 580:
            j = 0
            mz1 = 0
            mz2 = 0
            mz3 = 0
            mz4 = 0
            mz5 = 0
        pos = target_x1,target_y1
        width = 0
        radius = 10
        pygame.draw.circle(screen, red, pos, radius, width)
        width = 5
        radius = 20
        pygame.draw.circle(screen, red, pos, radius, width)
        radius = 30
        pygame.draw.circle(screen, red, pos, radius, width)
        drx = (shell_x - target_x1) ** 2
        dry = (shell_y - target_y1) ** 2
        if drx + dry <= 900 and  mz1 == 0:
            am += 20
            score += 4
            target_x1 = random.randint(270, 994)
            target_y1 = random.randint(80, 480)
            mz1 = 1
        if score < 80:
            pos = target_x2,target_y2
            width = 0
            radius = 10
            pygame.draw.circle(screen, black, pos, radius, width)
            width = 5
            radius = 20
            pygame.draw.circle(screen, black, pos, radius, width)
            radius = 30
            pygame.draw.circle(screen, black, pos, radius, width)
            drx = (shell_x - target_x2) ** 2
            dry = (shell_y - target_y2) ** 2
            if drx + dry <= 900 and mz2 == 0:
                score += 8
                target_x2 = random.randint(270, 994)
                target_y2 = random.randint(80, 480)
                mz2 = 1
        if score < 60:
            pos = target_x3,target_y3
            width = 0
            radius = 10
            pygame.draw.circle(screen, gold, pos, radius, width)
            width = 5
            radius = 20
            pygame.draw.circle(screen, gold, pos, radius, width)
            radius = 30
            pygame.draw.circle(screen, gold, pos, radius, width)
            drx = (shell_x - target_x3) ** 2
            dry = (shell_y - target_y3) ** 2
            if drx + dry <= 900 and mz3 == 0:
                am += 40
                score += 2
                target_x3 = random.randint(270, 994)
                target_y3 = random.randint(80, 480)
                mz3 = 1
        if score < 40:
            pos = target_x4,target_y4
            width = 0
            radius = 10
            pygame.draw.circle(screen, red, pos, radius, width)
            width = 5
            radius = 20
            pygame.draw.circle(screen, red, pos, radius, width)
            radius = 30
            pygame.draw.circle(screen, red, pos, radius, width)
            drx = (shell_x - target_x4) ** 2
            dry = (shell_y - target_y4) ** 2
            if drx + dry <= 900 and mz4 == 0:
                am += 20
                score += 4
                target_x4 = random.randint(270, 994)
                target_y4 = random.randint(80, 480)
                mz4 = 1
        if score < 20:
            pos = target_x5,target_y5
            width = 0
            radius = 10
            pygame.draw.circle(screen, gold, pos, radius, width)
            width = 5
            radius = 20
            pygame.draw.circle(screen, gold, pos, radius, width)
            radius = 30
            pygame.draw.circle(screen, gold, pos, radius, width)
            drx = (shell_x - target_x5) ** 2
            dry = (shell_y - target_y5) ** 2
            if drx + dry <= 900 and mz5 == 0:
                am += 40
                score += 2
                target_x5 = random.randint(270, 994)
                target_y5 = random.randint(80, 480)
                mz5 = 1
        screen.blit(tan, (tank_x,518))
        bx = tank_x + 60 - 10 * ars + 18 * arc
        ydy = 542 - 50 * ars - 10 * arc - 18 * ars
        gun_rotate = pygame.transform.rotate(gun, tank_a)
        screen.blit(gun_rotate, (bx,ydy))
        screen.blit(gro1, (0,560))
        imgText = myfont1.render("SCORE: " + str(score), True, black)
        screen.blit(imgText, (800,10))
        if am <= 0 and j == 0:
            i = 2  
    if i == 2:
        imgText = myfont2.render("SCORE: " + str(score), True, black)
        screen.blit(imgText, (400,300))
        if score >= 100:
            screen.blit(textImage8, (250,100))
        else:
            screen.blit(textImage9, (120,100))
        width = 0
        pos = 280, 400, 162, 100
        pygame.draw.rect(screen, red, pos, width)
        width = 5
        pygame.draw.rect(screen, black, pos, width)
        screen.blit(textImagea, (320,430))
        width = 0
        pos = 520, 400, 212, 100
        pygame.draw.rect(screen, red, pos, width)
        width = 5
        pygame.draw.rect(screen, black, pos, width)
        screen.blit(textImageb, (560,430))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_dx,mouse_dy = event.pos
                if mouse_dy <= 500 and mouse_dy >= 400:
                    if mouse_dx <= 442 and mouse_dx >= 280:
                        pygame.quit()
                        sys.exit()
                    elif mouse_dx <= 632 and mouse_dx >= 520:
                        score = 0
                        am = 240
                        pw = 0
                        i = 1
                        tank_x = 0
                        tank_a = 0
    pygame.display.update()