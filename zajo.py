"""
V tejto hre je Zajo ktory krokuje podla pravidiel
a ulohou je zisit kde skonci.
Ked dopadne na spravne policko tak sa spusti animacia ako
tam doskacka.
Pri prejdeni mysou nad kamen treba spravit animaciu.
TODO:
 - najst pekny font - spravit appku na zobrazenie vsetkych dostupnych ttf
 - spravit okno ked user zle klikne na kamen tak vypisat nieco take ako zle
"""
#imports
import pygame as pg
import sys
import random
from pygame.locals import *

#some useful constants
#info about window
WIN_WIDTH = 1024
WIN_HEIGHT = 768
#rock info
ROCK_LEFT_OFFSET = 180
ROCK_TOP_OFFSET = 500
ROCK_NUM = 8
#info about how many instructions will be used
INS_NUM = 10

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

#load images
grass_img = pg.image.load('grass.png')
bunny_img = pg.image.load('bunny.png ')
rock_img = pg.image.load('rock.png')
arrow_to_img = pg.image.load('arrow.png')
arrow_back_img = pg.transform.flip(arrow_to_img, True, False)

#bunny_img = pg.transform.scale(bunny_img, (150,150))
rock_img = pg.transform.scale(rock_img, (100,100))


#set height of rocks
h_rocks = []
for i in range(ROCK_NUM):
    h_rocks.append(ROCK_TOP_OFFSET + random.randint(0,80))

def main():
    pg.init()
    screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pg.display.set_caption('Zajko usko')

    running = True

    #set up the text
    intro_textObj = pg.font.SysFont('mistral', 46)
    intro_textSurfaceObj = intro_textObj.render('Klikni na kamen kde doskace Zajko podla pravidiel.', True, BLACK)
    intro_textRectObj = intro_textSurfaceObj.get_rect()
    intro_textRectObj.center = (WIN_WIDTH//2,100)

    #set up instructions
    ins, move_rock = create_ins()
    print(ins, move_rock)
    #mouse
    mouse_coor = [None, None]
    mouse_clicked = False

    while running:
        # fill the screen with the grass
        for x in range(int(WIN_WIDTH/grass_img.get_width()+1)):
            for y in range(int(WIN_HEIGHT/grass_img.get_height()+1)):
                screen.blit(grass_img, (x*grass_img.get_width(), y*grass_img.get_height()))
        # place bunny
        screen.blit(bunny_img, (-20,300))
        #place rocks
        for i in range(len(h_rocks)):
            y = h_rocks[i]
            x = i*100 + ROCK_LEFT_OFFSET
            screen.blit(rock_img, (x, y))
        #place text
        screen.blit(intro_textSurfaceObj, intro_textRectObj)
        #place instructions
        #this will calculate how much from left side will be the first square of instruction
        left_offset = (WIN_WIDTH - arrow_to_img.get_rect().size[0] * INS_NUM) // 2
        for i in range(len(ins)):
            if ins[i] == 1:
                screen.blit(arrow_to_img, (i*50 + left_offset, 200))
            elif ins[i] == 0:
                screen.blit(arrow_back_img, (i*50 + left_offset, 200))

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
            rockx, rocky = getRockAtPixel(*mouse_coor)
            if rockx != None and rocky != None:
                index = getRockIndex(rockx)
                if index == move_rock:
                    print('win')

def create_ins():
    ins = []
    move_rock = 0
    """
    move_rock obsahuje index na vysledny kamen.
    ins je pole, obsahuje instrukcie. Jedna znamena dopredu, nula spat.
     - Ten isty znak nemoze ist trikrat po sebe.
     - Prvy kamen zacina s indexom jeden
    posledny je ROCK_NUM.
     - Pokial je move_rock rovne 1, prida sa krok vpred.
     - Pokial je move_rock rovne ROCK_NUM,
     prida sa krok dozadu.
    Treba dodat ze najprv zajo nespravil ziaden krok tak
    move_rock bude najpv nula, potom sa to bude menit.
    Nemoze to byt ale nula lebo potom by zajo skoncil na mieste mimo kamena.
    """
    def all_same(items):
        return all(x == items[0] for x in items)

    for i in range(INS_NUM):
        if move_rock <= 1:
            ins.append(1)
            move_rock += 1
        elif move_rock == ROCK_NUM:
            ins.append(0)
            move_rock -= 1
        elif all_same(ins[-3:]) and len(ins[-3:]) == 3:
            ins.append(1 - ins[-1])
            if 1 - ins[-1] == 1:
                move_rock -= 1
            else:
                move_rock += 1
        else:
            r_num = random.randint(0,1)
            if r_num == 1:
                move_rock += 1
                ins.append(r_num)
            elif r_num == 0 and move_rock - 1 <= 1:
                move_rock += 1
                ins.append(1)
            else:
                move_rock -= 1
                ins.append(0)
        print(move_rock)
    return ins, move_rock

def getRockAtPixel(x,y):
    for rock in range(len(h_rocks)):
        hitBox = pg.Rect(rock*100+100, h_rocks[rock], 100, 100)
        if hitBox.collidepoint(x,y):
            return (rock*100+100, h_rocks[rock])
    return (None, None)

def getRockIndex(x):
    return (x-100)//100

if __name__ == "__main__":
    main()
