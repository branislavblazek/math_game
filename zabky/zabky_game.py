#import main libraries
from pygame.locals import *
import sys

from zabky.main_obj import Level, Zabka, Win

#import from sibling folder
sys.path.insert(0, "..")
import files

#initialize the constats
const = {}
const['game'] = None
const['color'] = files.colors.Consts_colors()
const['window'] = files.window.Consts_window()

def zabky_level(pg, screen, level_status, level_max):
    mouse_clicked = False
    mouse_coor = (0,0)
    #init the main object
    level = Level(level_status, pg)
    clock = pg.time.Clock()
    #get images
    images = level.load_images(const['window'].WIDTH, const['window'].HEIGHT)
    #zabky
    numbers = level.numbers_left
    frogs = []
    for i in range(len(numbers)):
        frogs.append(Zabka(numbers[i], pg, 80*i))
    #------------MAIN LOOP
    exit_code = -1
    zabiek_na_dreve = 0
    win_animacia = Win(pg, screen)
    while True:
        #---------PLACE IMAGES
        #set backgrund image
        screen.blit(images['farm'], (0,0))
        #set log end
        screen.blit(images['log_end'], (const['window'].WIDTH//3-120, 500))
        #set log
        screen.blit(images['log'], (const['window'].WIDTH//3-300, 390))
        #set box
        screen.blit(images['box'], (610, 400))
        #set weight
        #screen.blit(images['weight'], (65,300))
        images['weight'].draw(screen)
        #info level
        for star in range(level_max):
            if star < level_status:
                screen.blit(images['star_full'], (star*60+20,25))
            else:
                screen.blit(images['star_null'], (star*60+20,25))
        #vaha na hojdacke
        spolu_na_hojdacke_vaha = 0
        #set frog
        for frog in frogs:
            if frog.as_rect().collidepoint(mouse_coor) and mouse_clicked:
                mouse_clicked = False
                if frog.jump_direction == -1:
                    frog.is_jumping = True
                    zabiek_na_dreve += 1
                    frog.kolkata = zabiek_na_dreve
                    frog.max = level.left_side_n
            frog.kresli_info.draw(screen)
            spolu_na_hojdacke_vaha += frog.na_hojdacke

        if zabiek_na_dreve >= 2:
            if spolu_na_hojdacke_vaha == level.left_side:
                exit_code = 1
            else:
                exit_code = 0
        else:
            if spolu_na_hojdacke_vaha == level.left_side:
                exit_code = 1

        if mouse_clicked:
            mouse_clicked = False

        if exit_code == 1 or exit_code == 0:
            can_return = True
            for frog in frogs:
                if frog.is_jumping:
                    can_return = False

            if can_return:
                win_animacia.animate()
                if not win_animacia.is_animating:
                    return exit_code

        #---------EVENTS
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_coor = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_coor = event.pos
                mouse_clicked = True
        pg.display.update()
        clock.tick(60)
