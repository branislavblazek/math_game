import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello world!')


WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)

fontObj = pygame.font.SysFont('impact', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)


while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
