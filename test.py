import pygame
from pygame.locals import *

width = 1000
height = 900
speed = [2, 2]
GREEN = (150, 255, 150)
running = True
pygame.init()
screen = pygame.display.set_mode((width, height))
ball = pygame.image.load("yes.gif").convert_alpha()
ballrect = ball.get_rect()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill(GREEN)
    screen.blit(ball, ballrect)
    pygame.display.flip()
pygame.quit()
