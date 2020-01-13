import pygame
from pygame.locals import *
import sys
import random
from krokovanie import zajo_main

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ahoj svet')

def game_intro():
    text_one = pygame.font.Font('freesansbold.ttf', 115)
    surface_one = text_one.render('Ahojsvet', True, green)
    text_obj = surface_one.get_rect()
    text_obj.center = (400,300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coors = event.pos
                if text_obj.collidepoint(coors):
                    game_loop()

        screen.fill(white)
        screen.blit(surface_one, text_obj)
        pygame.display.update()

def game_loop():
    rect = pygame.Rect(0,0,100,100)
    catx = 0
    caty = 0
    valuex = 1
    valuey = 1
    max_width = display_width - 150
    max_height = display_height - 150
    cat_img = pygame.image.load('unicorn.png')

    while True:
        screen.fill(green)
        pygame.draw.rect(screen, black, rect)

        catx += valuex
        caty += valuey

        if catx >= max_width or catx < 0:
            valuex = -valuex
        if caty >= max_height or caty < 0:
            valuey = -valuey

        screen.blit(cat_img, (catx, caty))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coors = event.pos
                if rect.collidepoint(coors):
                    return False

        pygame.display.update()

game_intro()
