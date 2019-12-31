"""
V tejto hre je Zajo ktory krokuje podla pravidiel
a ulohou je zisit kde skonci.
Ked dopadne na spravne policko tak sa spusti animacia ako
tam doskacka.
V tejto hre budu levely, v kazdom leveli sa vytvori objekt.
TODO:
 - najst pekny font - spravit appku na zobrazenie vsetkych dostupnych ttf
 - spravit okno ked user zle klikne na kamen tak vypisat nieco take ako zle
 - spravit animaciu nad kamenom
 - na zaciatku kazdeho levelu sa kamena animuju na svoje miestoF
"""
#imports
import pygame as pg
import sys
import random
from pygame.locals import *
from main_obj import Level
from consts import Consts_game, Consts_colors

#initialize the constants
consts = Consts_game()
consts_color = Consts_colors()

def getRockIndex(x):
    return x // consts.ROCK_WIDTH

def main():
    pg.init()
    screen = pg.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))
    pg.display.set_caption(consts.WIN_TITLE)

    #init the object
    level = Level(1, pg)
    #get height for rocks
    h_rocks = level.random_rock_height(consts.ROCK_NUM, consts.ROCK_TOP_OFFSET)
    #get images and get height of rocks
    images, consts.rock_height = level.load_images(consts.ROCK_WIDTH)
    #set up the text
    intro_text, intro_rect = level.generate_text(consts.WIN_WIDTH, consts_color.BLACK)
    #set up the numbers
    numbers_text, numbers_rect = level.generate_numbers(consts.ROCK_WIDTH, consts_color.RED, consts.ROCK_NUM + 1)
    #set up instructions
    ins, move_rock = level.create_ins(consts.ins_num, consts.ROCK_NUM)
    ins_num = len(ins)
    print(move_rock)
    #mouse
    mouse_coor = [None, None]
    mouse_clicked = False
    #run the game
    level.gameRunning = True
    while level.gameRunning:
        # fill the screen with the grass
        for x in range(int(consts.WIN_WIDTH/images["grass"].get_width()+1)):
            for y in range(int(consts.WIN_HEIGHT/images["grass"].get_height()+1)):
                screen.blit(images["grass"], (x*images["grass"].get_width(), y*images["grass"].get_height()))
        # place start rock
        screen.blit(images["rock"], (0,460))
        # place bunny
        screen.blit(images["bunny"], (0,260))
        #place rocks
        for i in range(len(h_rocks)):
            y = h_rocks[i]
            x = i * consts.ROCK_WIDTH + consts.ROCK_WIDTH
            screen.blit(images["rock"], (x, y))
        #place numbers under rocks
        for i in range(consts.ROCK_NUM + 1):
            screen.blit(numbers_text[i], numbers_rect[i])
        #place text
        screen.blit(intro_text, intro_rect)
        #place instructions
        left_offset = (consts.WIN_WIDTH - images["arrow_to"].get_rect().size[0] * consts.ins_num) // 2
        for i in range(len(ins)):
            if ins[i] == 1:
                screen.blit(images["arrow_to"], (i*50 + left_offset, 200))
            elif ins[i] == 0:
                screen.blit(images["arrow_back"], (i*50 + left_offset, 200))

        pg.display.flip()

        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()
                pg.quit()
            elif event.type == MOUSEMOTION:
                mouse_coor = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_coor = event.pos
                mouse_clicked = True

        if mouse_clicked:
            #this will prevent to run this condition several times
            mouse_clicked = False
            rockx, rocky = level.getRockAtPixel(*mouse_coor, h_rocks, consts.ROCK_WIDTH, consts.rock_height)
            if rockx != None and rocky != None:
                index = getRockIndex(rockx)
                if index == move_rock:
                    print('win')
                    level.gameRunning = False

if __name__ == "__main__":
    main()
