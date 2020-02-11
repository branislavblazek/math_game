import pygame
from pygame.locals import *
import sys
import random
from krokovanie.zajo_main import zajo_main_func
from zabky.zabky_main import zabky_main_func
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

screen = pygame.display.set_mode((const['window'].WIDTH, 650))
pygame.display.set_caption('ahoj svet' + str(pygame.display.Info().current_h))

def game_intro():
    screen_type = 1 if pygame.display.Info().current_h > 768 else 2 #if pygame.display.Info().current_h <= 768

    mouse_coors = [0,0]
    text_one = pygame.font.Font('freesansbold.ttf', 115)

    #------PRVY DOMCEK
    game1 = pygame.image.load('resources/home.png')
    game1_maskot = pygame.image.load('krokovanie/resources/bunny.png')
    if screen_type == 1:
        game1_maskot_obj = files.intro_obj.Mascot_animation((240,414))
        game1_rect.topleft = (30,400)
    elif screen_type == 2:
        game1 = pygame.transform.scale(game1, (450,258))
        game1_rect = game1.get_rect()
        game1_rect.topleft = (90,340)
        game1_maskot = pygame.transform.scale(game1_maskot, (101,194))
        game1_maskot_obj = files.intro_obj.Mascot_animation((260,385))

    #------DRUHY DOMCEK
    game2 = pygame.image.load('resources/home.png')
    game2_maskot = pygame.image.load('zabky/resources/frog.png')
    if screen_type == 1:
        game2_maskot = pygame.transform.scale(game2_maskot, (135, 173))
        game2_maskot_obj = files.intro_obj.Mascot_animation((630, 200))
        game2_maskot_obj.max_off = 140
        game2_rect = game2.get_rect()
        game2_rect.topleft = (420, 140)
    elif screen_type == 2:
        game2 = pygame.transform.scale(game2, (450,258))
        game2_maskot = pygame.transform.scale(game2_maskot, (113, 120))
        game2_maskot_obj = files.intro_obj.Mascot_animation((670, 200))
        game2_maskot_obj.max_off = 60
        game2_rect = game2.get_rect()
        game2_rect.topleft = (520, 190)

    #-----TRETI DOMCEK
    game3 = pygame.image.load('resources/home2.png')
    game3_rect = game3.get_rect()
    game3_rect.topleft = (-70, 0)
    if screen_type == 2:
        game3 = pygame.transform.scale(game3, (450,258))
        game3_rect = game3.get_rect()
        game3_rect.topleft = (150, 20)

    autor_textObj = pygame.font.SysFont('verdana', 16)
    autor_textSurfaceObj = autor_textObj.render('Verbová Nikola, Blažek Branislav', True, const['colors'].BLACK)
    autor_textRectObj = autor_textSurfaceObj.get_rect()
    autor_textRectObj.center = (pygame.display.Info().current_w-140,pygame.display.Info().current_h-16)

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
            #-----CLICK EVENT
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coors = event.pos
                if game1_rect.collidepoint(mouse_coors):
                    #-----START ZAJO
                    zajo_main_func(pygame, screen)
                elif game2_rect.collidepoint(mouse_coors):
                    #-----START ZABKY
                    zabky_main_func(pygame, screen)

        screen.fill((242, 225, 155))
        screen.blit(game3, game3_rect)
        screen.blit(game1_maskot, game1_maskot_obj.position())
        screen.blit(game1, game1_rect)
        screen.blit(game2_maskot, game2_maskot_obj.position())
        screen.blit(game2, game2_rect)
        screen.blit(autor_textSurfaceObj, autor_textRectObj)
        pygame.display.update()

game_intro()
