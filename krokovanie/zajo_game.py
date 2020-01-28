"""
V tejto hre je Zajo ktory krokuje podla pravidiel
a ulohou je zisit kde skonci.
V tejto hre budu levely, v kazdom leveli sa vytvori objekt.
"""
#import main libraries
from pygame.locals import *
import sys
import random

#import consts
from krokovanie.main_obj import Level
from krokovanie.consts import Consts_game

#import from sibling folder
sys.path.insert(0, "..")
import files

#initialize the constants
const = {}
const['game'] = Consts_game()
const['color'] = files.colors.Consts_colors()
const['window'] = files.window.Consts_window()

def getRockIndex(x):
    return x // const['game'].ROCK_WIDTH

def zajo_level(pg, screen, level_status, level_max):
    #init the object
    level = Level(level_status, pg)
    clock = pg.time.Clock()
    #get height for rocks
    level.random_rock_height(const['game'].ROCK_NUM, const['game'].ROCK_TOP_OFFSET)
    #get images and get height of rocks
    images, const['game'].rock_height = level.load_images(const['game'].ROCK_WIDTH)
    #set up the text
    intro_text, intro_rect = level.generate_text(const['window'].WIDTH, const['color'].BLACK)
    #set up the numbers
    numbers_text, numbers_rect = level.generate_numbers(const['game'].ROCK_WIDTH, const['color'].RED, const['game'].ROCK_NUM + 1)
    #set up instructions
    ins, move_rock = level.create_ins(const['game'].ins_num, const['game'].ROCK_NUM)
    ins_num = len(ins)
    #mouse
    mouse_coor = [0, 0]
    mouse_clicked = False
    count_jump = -1

    #main loop
    level.start = True
    while True:
        # fill the screen with the grass
        for x in range(int(const['window'].WIDTH/images["grass"].get_width()+1)):
            for y in range(int(const['window'].HEIGHT/images["grass"].get_height()+1)):
                screen.blit(images["grass"], (x*images["grass"].get_width(), y*images["grass"].get_height()))
        # place level info
        #screen.blit(level_font_surface, level_font_rect)
        for star in range(level_max):
            if star < level_status:
                screen.blit(images['star_full'], (star*60+20,25))
            else:
                screen.blit(images['star_null'], (star*60+20,25))

        # place start rock
        screen.blit(images["rock"], level.rocks_coors(0,460, -2))
        #place rocks
        for i in range(len(level.h_rocks)):
            y = level.h_rocks[i]
            x = i * const['game'].ROCK_WIDTH + const['game'].ROCK_WIDTH
            screen.blit(images["rock"], level.rocks_coors(x,y, i))

        level.start_anim()

        if count_jump > 0 and level.isJumping == False:
            level.isJumping = True
            level.index_rock_jump = move_rock - count_jump
            count_jump -= 1
            level.now_on_index += 1
        elif count_jump == 0 and level.isJumping == False:
            level.index_rock_jump = move_rock - count_jump
            level.now_on_index += 1
            count_jump -= 1

        #place numbers under rocks
        for i in range(const['game'].ROCK_NUM + 1):
            new_rect = numbers_rect[i].copy()
            is_last = True if i == const['game'].ROCK_NUM else False
            new_rect[1] = level.numbers_coors(new_rect[1], is_last)
            screen.blit(numbers_text[i], new_rect)
        #place text
        screen.blit(intro_text, intro_rect)
        #place instructions
        left_offset = (const['window'].WIDTH - images["arrow_to"].get_rect().size[0] * const['game'].ins_num) // 2
        for i in range(len(ins)):
            if ins[i] == 1:
                screen.blit(images["arrow_to"], (i*50 + left_offset, 200))
            elif ins[i] == 0:
                screen.blit(images["arrow_back"], (i*50 + left_offset, 200))

        # place bunny
        screen.blit(images["bunny"], level.bunny_coors())
        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()
                pg.quit()
            elif event.type == MOUSEMOTION:
                mouse_coor = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_coor = event.pos
                mouse_clicked = True

        rockx, rocky = level.getRockAtPixel(*mouse_coor, const['game'].ROCK_WIDTH, const['game'].rock_height)
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
                    level.correct = True
                else:
                    level.correct = False

                level.isJumping = True
                level.index_rock_jump = 0
                count_jump = index - 1
                #print('index: ' + str(index) + ' moverock: ' +  str(move_rock))
                level.going_to_jump = count_jump

        #end game
        if level.now_on_index == level.going_to_jump and level.correct:
            return 'status'
        elif level.now_on_index == level.going_to_jump and level.correct == False:
            return 'max'

        #update display
        pg.display.update()
        clock.tick(60)
