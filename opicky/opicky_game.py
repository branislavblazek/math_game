from opicky.main_obj import Level
from pygame.locals import *
import sys

#import from sibling folder
sys.path.insert(0, "..")
import files

#initialize the constats
const = {}
const['game'] = None
const['color'] = files.colors.Consts_colors()
const['window'] = files.window.Consts_window()

def opicky_level(pg, screen, level_status, level_max):
    clock = pg.time.Clock()
    level = Level(pg)
    #actions
    mouse_clicked = False
    mouse_coor = (0,0)
    #get images
    images = level.load_images()
    #exit
    exit_code = -1
    #-------HOME BUTTON
    images['back_rect'].topleft = (0,pg.display.Info().current_h-images['back'].get_height())

    surface_home = pg.Surface((images['back'].get_width(), images['back'].get_height()))
    surface_home.set_alpha(128)
    surface_home.fill((0, 149, 255))
    surface_home_rect = surface_home.get_rect()
    
    #-------HELPING
    level.start_pos = [const['window'].WIDTH-images['q_mark'].get_width(), 0]
    level.act_pos = level.start_pos.copy()

    surface_help = pg.Surface((300,images['q_mark'].get_height()))
    surface_help.set_alpha(128)
    surface_help.fill((0, 149, 255))
    surface_help_rect = surface_help.get_rect()

    text_help_font = pg.font.Font('freesansbold.ttf', 32)
    medzera = "         " if 9 < 10 else "       "
    text_help_surface = text_help_font.render(str(9) + ' =' + medzera +  '+       ', True, const['color'].BLACK)
    text_help_rect = text_help_surface.get_rect()

    #frog_help = images['help_frog']
    #frog_help_rect = frog_help.get_rect()

    #-------MAIN LOOP
    while True:
        #PLACE SOME IMAGES
        #backgorund image
        screen.blit(images['jungle'], (0,0))

        #home
        surface_home_rect[0] = pg.display.Info().current_w - images['back'].get_width()
        surface_home_rect[1] = pg.display.Info().current_h - images['back'].get_height()
        images['back_rect'][0] = pg.display.Info().current_w - images['back'].get_width()
        images['back_rect'][1] = pg.display.Info().current_h - images['back'].get_height()
        screen.blit(surface_home, surface_home_rect)
        screen.blit(images['back'], images['back_rect'])   

        #HELPING
            #rect
        surface_help_rect[0] = level.act_pos[0]
        surface_help_rect[1] = level.act_pos[1]
        screen.blit(surface_help, surface_help_rect)
            #set ask
        images['q_mark_rect'].topleft = level.act_pos
        screen.blit(images['q_mark'], images['q_mark_rect'])
            #text
        text_help_rect.topleft = (level.act_pos[0] + images['q_mark'].get_width(), 20)
        screen.blit(text_help_surface, text_help_rect)
            #frogs
        #frog_help_rect.topleft = (level.act_pos[0] + images['q_mark'].get_width() + 70, 10)
        #screen.blit(frog_help, frog_help_rect)
        #frog_help_rect.topleft = (level.act_pos[0] + images['q_mark'].get_width() + 150, 10)
        #screen.blit(frog_help, frog_help_rect)

        #info level
        for star in range(level_max):
            if star < level_status:
                screen.blit(images['banana_full'], (star * 80 + 20, 25))
            else:
                screen.blit(images['banana_null'], (star * 80 + 20, 25))

        #MOUSE ACTIONS
        #over home button
        if surface_home_rect.collidepoint(mouse_coor):
            surface_home.fill(const['color'].YELLOW)
        else:
            surface_home.fill(const['color'].BLUE)

        if images['back_rect'].collidepoint(mouse_coor) and mouse_clicked:
            return 2
        
        #over help
        if surface_help_rect.collidepoint(mouse_coor):
            if level.act_pos[0] >= level.start_pos[0] - level.max_off:
                level.act_pos[0] -= 6
        else:
            if level.act_pos[0] < level.start_pos[0]:
                level.act_pos[0] += 6

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_coor = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_coor = event.pos
                mouse_clicked = True

        pg.display.flip()
        clock.tick(60)