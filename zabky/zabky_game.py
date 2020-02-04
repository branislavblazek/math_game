#import main libraries
from pygame.locals import *
import sys

from zabky.main_obj import Level, Zabka

#import from sibling folder
sys.path.insert(0, "..")
import files

#initialize the constats
const = {}
const['game'] = None
const['color'] = files.colors.Consts_colors()
const['window'] = files.window.Consts_window()

def zabky_level(pg, screen, level_status):
    mouse_clicked = False
    mouse_coor = (0,0)
    #init the main object
    level = Level(level_status, pg)
    #get images
    images = level.load_images(const['window'].WIDTH, const['window'].HEIGHT)
    #zabky
    frogs = []
    frogs.append(Zabka(15, pg))
    #------------MAIN LOOP
    while True:
        #---------PLACE IMAGES
        #set backgrund image
        screen.blit(images['farm'], (0,0))
        #set log end
        screen.blit(images['log_end'], (const['window'].WIDTH//3-100, 500))
        #set log
        screen.blit(images['log'], (const['window'].WIDTH//3-270, 390))
        #set box
        screen.blit(images['box'], (610, 420))
        #set weight
        #screen.blit(images['weight'], (65,300))
        images['weight'].draw(screen)
        #vaha na hojdacke
        spolu_na_hojdacke_vaha = 0
        #set frog
        for index, frog in enumerate(frogs):
            if frog.as_rect(index).collidepoint(mouse_coor) and mouse_clicked:
                mouse_clicked = False
                frog.is_jumping = True
            frog.kresli_info.draw(screen)
            spolu_na_hojdacke_vaha += frog.na_hojdacke
        print(spolu_na_hojdacke_vaha)

        #---------EVENTS
        for event in pg.event.get():
            if event.type == QUIT:
                pq.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_coor = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_coor = event.pos
                mouse_clicked = True
        pg.display.update()
