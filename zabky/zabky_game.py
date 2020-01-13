#import main libraries
from pygame.locals import *
import sys

from main_obj import Level

#import from sibling folder
sys.path.insert(0, "..")
import files

#initialize the constats
const = {}
const['game'] = None
const['color'] = files.colors.Consts_colors()
const['window'] = files.window.Consts_window()

def zabky_level(pg, screen, level_status):
    #init the main object
    level = Level(level_status, pg)
    #get images
    images = level.load_images(const['window'].WIDTH, const['window'].HEIGHT)
    #------------MAIN LOOP
    while True:
        #---------PLACE IMAGES
        #set backgrund image
        screen.blit(images['farm'], (0,0))
        #set log end
        screen.blit(images['log_end'], (const['window'].WIDTH//3-(170//2), 580))
        #set log
        screen.blit(images['log'], (100,480))

        #---------EVENTS
        for event in pg.event.get():
            if event.type == QUIT:
                pq.quit()
                sys.exit()
        pg.display.flip()
