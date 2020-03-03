import pygame
from pygame.locals import *
import sys
import random
import time

from krokovanie.zajo_main import zajo_main_func
from zabky.zabky_main import zabky_main_func
from opicky.opicky_main import opicky_main_func

from files.window import Consts_window
from files.colors import Consts_colors
import files.intro_obj

pygame.init()

const = {
    'window': Consts_window(),
    'colors': Consts_colors()
}

height = const['window'].HEIGHT
#optimalizacie pre _x768 obrazovky
screen_height = pygame.display.Info().current_h
if screen_height <= 768:
    height = 650

screen = pygame.display.set_mode((const['window'].WIDTH, height))
pygame.display.set_caption(const['window'].TITLE)

def game_intro():
    clock = pygame.time.Clock()
    screen_type = 1 if pygame.display.Info().current_h > 700 else 2 #if pygame.display.Info().current_h <= 768

    mouse_coors = [0,0]

    #-----PODKLAD
    grass = pygame.image.load('resources/grass.png')
    grass = pygame.transform.scale(grass, (1143, 850))
    grass_rect = grass.get_rect()
    grass_rect.bottom = 768 if screen_type == 1 else 700
    #------CESTA
    road = pygame.image.load('resources/road3.png')
    road_down = road.copy()
    road_down = pygame.transform.rotozoom(road, 8, 1)
    road_down = pygame.transform.flip(road_down, True, True)
    road_middle = pygame.transform.flip(road, True, False)

    #------PRVY DOMCEK
    game1 = pygame.image.load('resources/home_left_free.png')
    game1 = pygame.transform.flip(game1, True, False)
    game1_maskot = pygame.image.load('krokovanie/resources/bunny.png')
    game1_rect = game1.get_rect()
    x1 = 10
    x2 = 410

    if screen_type == 1:
        #game1 = pygame.transform.scale(game1, (500,287))
        game1_maskot_obj = files.intro_obj.Mascot_animation((x1 + 215,x2 + 30))
        #game1_maskot = pygame.transform.scale(game1_maskot, (112, 215))
        game1_rect.topleft = (x1, x2)
        game1_maskot_obj.max_off = 200
    elif screen_type == 2:
        game1 = pygame.transform.scale(game1, (450,258))
        game1_rect = game1.get_rect()
        game1_rect.topleft = (120,340)
        game1_maskot = pygame.transform.scale(game1_maskot, (101,194))
        game1_maskot_obj = files.intro_obj.Mascot_animation((310,385))

    #------DRUHY DOMCEK
    game2 = pygame.image.load('resources/home_left_free.png')
    game2_maskot = pygame.image.load('zabky/resources/frog4.png')
    x1 = 480
    x2 = 190

    if screen_type == 1:
        game2_maskot_obj = files.intro_obj.Mascot_animation((x1 + 210, x2 + 60))
        game2_maskot_obj.max_off = 130
        game2_rect = game2.get_rect()
        game2_rect.topleft = (x1, x2)
    elif screen_type == 2:
        game2 = pygame.transform.scale(game2, (450,258))
        game2_maskot = pygame.transform.scale(game2_maskot, (113, 120))
        game2_maskot_obj = files.intro_obj.Mascot_animation((670, 200))
        game2_maskot_obj.max_off = 80
        game2_rect = game2.get_rect()
        game2_rect.topleft = (520, 190)

    #-----TRETI DOMCEK
    game3 = pygame.image.load('resources/home.png')
    game3 = pygame.transform.flip(game3, True, False)
    game3_maskot = pygame.image.load('opicky/resources/monkey_home.png')
    game3_maskot = pygame.transform.rotozoom(game3_maskot, -44, 1)
    game3_rect = game3.get_rect()
    x1 = -100
    x2 = 10
    game3_rect.topleft = (x1, x2)

    if screen_type == 1:
        game3_maskot_obj = files.intro_obj.Mascot_animation((x1 + 300, x2 + 42), True)
        game3_maskot_obj.max_off = 100
    elif screen_type == 2:
        game3 = pygame.transform.scale(game3, (450,258))
        game3_rect = game3.get_rect()
        game3_rect.topleft = (10, 20)
        game3_maskot_obj = files.intro_obj.Mascot_animation((x1, x2))

    #-----AUTORI
    autor_textObj = pygame.font.SysFont('verdana', 16)
    autor_textSurfaceObj = autor_textObj.render('Blažek Branislav, Verbová Nikola', True, const['colors'].BLACK)
    autor_textRectObj = autor_textSurfaceObj.get_rect()
    autor_textRectObj.center = (pygame.display.Info().current_w-140,pygame.display.Info().current_h-16)

    #-----NAZOV
    nazov_font = pygame.font.SysFont('verdana', 75, True)
    nazov_surface = nazov_font.render(const['window'].TITLE, True, const['colors'].RED)
    nazov_rect = nazov_surface.get_rect()
    nazov_rect.center = (780, 70)

    while True:
        #------MAIN LOOP
        for event in pygame.event.get():
            #------QUIT EVENT
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #-----MOUTION EVENT
            elif event.type == pygame.MOUSEMOTION:
                mouse_coors = event.pos
                if game1_rect.collidepoint(mouse_coors):
                    game1_maskot_obj.is_showing = True
                    game1_maskot_obj.is_hiding = False
                    game1_maskot_obj.is_hided = False
                else:
                    game1_maskot_obj.is_showing = False
                    game1_maskot_obj.is_showed = False
                    game1_maskot_obj.is_hiding = True

                if game2_rect.collidepoint(mouse_coors):
                    game2_maskot_obj.is_showing = True
                    game2_maskot_obj.is_hiding = False
                    game2_maskot_obj.is_hided = False
                else:
                    game2_maskot_obj.is_showing = False
                    game2_maskot_obj.is_showed = False
                    game2_maskot_obj.is_hiding = True

                if game3_rect.collidepoint(mouse_coors):
                    game3_maskot_obj.is_showing = True
                    game3_maskot_obj.is_hiding = False
                    game3_maskot_obj.is_hided = False
                else:
                    game3_maskot_obj.is_showing = False
                    game3_maskot_obj.is_showed = False
                    game3_maskot_obj.is_hiding = True
                    
            #-----CLICK EVENT
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coors = event.pos
                if game1_rect.collidepoint(mouse_coors):
                    #-----START ZAJO
                    zajo_main_func(pygame, screen)
                elif game2_rect.collidepoint(mouse_coors):
                    #-----START ZABKY
                    zabky_main_func(pygame, screen)
                elif game3_rect.collidepoint(mouse_coors):
                    #-----START OPICKY
                    opicky_main_func(pygame, screen)
                    
        screen.blit(grass, grass_rect)

        if screen_type == 1:
            screen.blit(road_down, (170,490))
            screen.blit(road_middle, (80,270))
        elif screen_type == 2:
            screen.blit(road_down, (140,400))
            screen.blit(road_middle, (130,190))

        screen.blit(game3_maskot, game3_maskot_obj.position())
        screen.blit(game3, game3_rect)
        screen.blit(game1_maskot, game1_maskot_obj.position())
        screen.blit(game1, game1_rect)
        screen.blit(game2_maskot, game2_maskot_obj.position())
        screen.blit(game2, game2_rect)
        screen.blit(autor_textSurfaceObj, autor_textRectObj)
        screen.blit(nazov_surface, nazov_rect)

        pygame.display.update()
        clock.tick(60)

game_intro()
