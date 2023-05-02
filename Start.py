import math

import pygame
from pygame import Rect

# methods

# variables
rect_mouse = Rect(-50, -50, 50, 50)
rect_AB = Rect(0, 0, 0, 0)
rect_CD = Rect(0, 0, 0, 0)
pos = [300, 300]
size = [100, 100]

planet = [600, 400, 50]
moon = [800, 600, 20, 0, 0]
moon2 = [900, 700, 20, 0, 0]
angle = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # keys that checks for keys being pressed

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                temp_mouse_loc = pygame.mouse.get_pos()
                rect_mouse.update(pygame.mouse.get_pos(), (0, 0))
        if event.type == pygame.MOUSEBUTTONUP:
            temp_mouse_loc = None
            rect_mouse.update(0, 0, 0, 0)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    if pygame.mouse.get_pressed(3)[0]:
        if pygame.mouse.get_pos()[1] - temp_mouse_loc[1] < 0 and pygame.mouse.get_pos()[0] - temp_mouse_loc[0] < 0:
            rect_mouse.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                              temp_mouse_loc[0] - pygame.mouse.get_pos()[0],
                              temp_mouse_loc[1] - pygame.mouse.get_pos()[1])
        elif pygame.mouse.get_pos()[0] - temp_mouse_loc[0] < 0:
            rect_mouse.update(pygame.mouse.get_pos()[0],
                              temp_mouse_loc[1],
                              temp_mouse_loc[0] - pygame.mouse.get_pos()[0],
                              (pygame.mouse.get_pos()[1] - temp_mouse_loc[1]))
        elif pygame.mouse.get_pos()[1] - temp_mouse_loc[1] < 0:
            rect_mouse.update(temp_mouse_loc[0], pygame.mouse.get_pos()[1],
                              pygame.mouse.get_pos()[0] - temp_mouse_loc[0],
                              temp_mouse_loc[1] - pygame.mouse.get_pos()[1])
        else:
            rect_mouse.update(temp_mouse_loc, (
                pygame.mouse.get_pos()[0] - temp_mouse_loc[0], pygame.mouse.get_pos()[1] - temp_mouse_loc[1]))
        if temp_mouse_loc[0] != 0 and temp_mouse_loc[1] != 0 and pygame.mouse.get_pos()[0] != 0 and \
                pygame.mouse.get_pos()[1] != 0:
            rect_AB.update(temp_mouse_loc[0] - 5, temp_mouse_loc[1] - 5, 10, 10)
            rect_CD.update(pygame.mouse.get_pos()[0] - 5, pygame.mouse.get_pos()[1] - 5, 10, 10)

    # do the engine here

    # RENDER YOUR GAME HERE

    pygame.draw.circle(screen, '#ff0000', (planet[0], planet[1]), planet[2])
    pygame.draw.circle(screen, '#00ff00', (moon[3], moon[4]), moon[2])
    pygame.draw.circle(screen, '#00ffff', (moon2[3], moon2[4]), moon2[2])

    # calc
    # planet = [200, 200, 50]
    # moon = [400, 400, 20, 600, 200]
    angle += 2
    #planet[0] += math.cos(.01*angle)
    #planet[1] += math.sin(.01*angle)
    #moon[0] += math.cos(.01*angle)
    #moon[1] += math.sin(.01*angle)
    moon[3] = (moon[0] - planet[0]) * math.cos(.1*angle*0.05)+planet[0]
    moon[4] = (moon[1] - planet[1]) * math.sin(.1*angle*0.05)+planet[1]
    moon2[3] = (moon2[0] - planet[0]) * math.cos(angle * 0.005) + planet[0]
    moon2[4] = (moon2[1] - planet[1]) * math.sin(angle * 0.005) + planet[1]

    pygame.draw.rect(screen, '#ff0000', rect_mouse)
    pygame.draw.rect(screen, '#00aa00', rect_AB)
    pygame.draw.rect(screen, '#0000aa', rect_CD)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
