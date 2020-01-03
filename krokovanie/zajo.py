"""
V tejto hre je Zajo ktory krokuje podla pravidiel
a ulohou je zisit kde skonci.
V tejto hre budu levely, v kazdom leveli sa vytvori objekt.
TODO:
 - najst pekny font - spravit appku na zobrazenie vsetkych dostupnych ttf]
 - najst pekne pozadie pre hru
 - spravit win akciu
 - hodia sa tu levely
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
    level.random_rock_height(consts.ROCK_NUM, consts.ROCK_TOP_OFFSET)
    #get images and get height of rocks
    images, consts.rock_height = level.load_images(consts.ROCK_WIDTH)
    #set up the text
    intro_text, intro_rect = level.generate_text(consts.WIN_WIDTH, consts_color.BLACK)
    #set up the numbers
    numbers_text, numbers_rect = level.generate_numbers(consts.ROCK_WIDTH, consts_color.RED, consts.ROCK_NUM + 1)
    #set up instructions
    ins, move_rock = level.create_ins(consts.ins_num, consts.ROCK_NUM)
    ins_num = len(ins)
    print('correct answer: ' + str(move_rock))
    #mouse
    mouse_coor = [None, None]
    mouse_clicked = False
    count_jump = -1
    #run the game
    level.gameRunning = True
    while level.gameRunning:
        # fill the screen with the grass
        for x in range(int(consts.WIN_WIDTH/images["grass"].get_width()+1)):
            for y in range(int(consts.WIN_HEIGHT/images["grass"].get_height()+1)):
                screen.blit(images["grass"], (x*images["grass"].get_width(), y*images["grass"].get_height()))
        # place start rock
        screen.blit(images["rock"], level.rocks_coors(0,460, -2))
        #place rocks
        for i in range(len(level.h_rocks)):
            y = level.h_rocks[i]
            x = i * consts.ROCK_WIDTH + consts.ROCK_WIDTH
            screen.blit(images["rock"], level.rocks_coors(x,y, i))

        level.start_anim()

        if count_jump > 0 and level.isJumping == False:
            level.isJumping = True
            level.index_rock_jump = move_rock - count_jump
            count_jump -= 1
        elif count_jump == 0 and level.isJumping == False:
            level.index_rock_jump = move_rock - count_jump
            count_jump -= 1

        #place numbers under rocks
        for i in range(consts.ROCK_NUM + 1):
            new_rect = numbers_rect[i].copy()
            new_rect[1] = level.numbers_coors(new_rect[1])
            screen.blit(numbers_text[i], new_rect)

        #place text
        screen.blit(intro_text, intro_rect)

        #place instructions
        left_offset = (consts.WIN_WIDTH - images["arrow_to"].get_rect().size[0] * consts.ins_num) // 2
        for i in range(len(ins)):
            if ins[i] == 1:
                screen.blit(images["arrow_to"], (i*50 + left_offset, 200))
            elif ins[i] == 0:
                screen.blit(images["arrow_back"], (i*50 + left_offset, 200))

        # place bunny
        screen.blit(images["bunny"], level.bunny_coors())

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

        rockx, rocky = level.getRockAtPixel(*mouse_coor, consts.ROCK_WIDTH, consts.rock_height)
        if rockx != None and rocky != None and not level.isJumping:
            index = getRockIndex(rockx) - 1
            if index != level.rock_hover_index:
                level.rock_old_hover_index = level.rock_hover_index
                level.rock_old_hover_pos = level.rock_old_hover_height
                level.rock_hover_index = index
                level.rock_hover_pos = 0
        elif level.rock_hover_index != -1 and not level.isJumping:
            level.rock_old_hover_index = level.rock_hover_index
            level.rock_old_hover_pos = level.rock_old_hover_height
            level.rock_hover_index = -1

        if mouse_clicked and not level.isJumping:
            #this will prevent to run this condition several times
            mouse_clicked = False
            if rockx != None and rocky != None:
                index = getRockIndex(rockx)
                if index == move_rock:
                    level.isJumping = True
                    level.index_rock_jump = 0
                    count_jump = move_rock - 1
                    print('teraz treba dorobit co sa stane')
                else:
                    level.shake_index = index - 1


if __name__ == "__main__":
    main()
