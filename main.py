import pygame
from pygame.locals import *
import sys
import random
from krokovanie.zajo_main import zajo_main_func
from zabky.zabky_main import zabky_main_func

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

    surface_one = text_one.render('prva_hra', True, green)
    surface_two = text_one.render('druha_hra', True, red)

    text_obj_one = surface_one.get_rect()
    text_obj_one.center = (400, 150)

    text_obj_two = surface_two.get_rect()
    text_obj_two.center = (400, 450)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coors = event.pos
                if text_obj_one.collidepoint(coors):
                    zajo_main_func(pygame, screen)
                elif text_obj_two.collidepoint(coors):
                    zabky_main_func(pygame, screen)

        screen.fill(white)
        screen.blit(surface_one, text_obj_one)
        screen.blit(surface_two, text_obj_two)
        pygame.display.update()

#def game_loop():
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
