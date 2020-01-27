import pygame
from pygame.locals import *
import sys
import random
from krokovanie.zajo_main import zajo_main_func
from zabky.zabky_main import zabky_main_func
from files.window import Consts_window
from files.colors import Consts_colors

pygame.init()

const = {
    'window': Consts_window(),
    'colors': Consts_colors()
}

screen = pygame.display.set_mode((const['window'].WIDTH, const['window'].HEIGHT))
pygame.display.set_caption('ahoj svet')

def game_intro():
    text_one = pygame.font.Font('freesansbold.ttf', 115)

    surface_one = text_one.render('prva_hra', True, const['colors'].BLUE)
    surface_two = text_one.render('druha_hra', True, const['colors'].GREEN)

    text_obj_one = surface_one.get_rect()
    text_obj_one.center = (400, 150)

    text_obj_two = surface_two.get_rect()
    text_obj_two.center = (400, 450)

    while True:
        #------MAIN LOOP
        for event in pygame.event.get():
            #------QUIT EVENT
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #-----CLICK EVENT
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coors = event.pos
                if text_obj_one.collidepoint(coors):
                    #-----START ZAJO
                    zajo_main_func(pygame, screen)
                elif text_obj_two.collidepoint(coors):
                    #-----START ZABKY
                    zabky_main_func(pygame, screen)

        screen.fill(const['colors'].WHITE)
        screen.blit(surface_one, text_obj_one)
        screen.blit(surface_two, text_obj_two)
        pygame.display.update()

game_intro()
