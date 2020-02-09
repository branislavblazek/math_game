#import main libraries
from pygame.locals import *
import sys

from zabky.main_obj import Level, Zabka, Win, Lose

#import from sibling folder
sys.path.insert(0, "..")
import files

#initialize the constats
const = {}
const['game'] = None
const['color'] = files.colors.Consts_colors()
const['window'] = files.window.Consts_window()

def zabky_level(pg, screen, level_status, level_max, left_side, right_side):
    mouse_clicked = False
    mouse_coor = (0,0)
    #init the main object
    level = Level(level_status, pg)
    level.left_side = left_side
    level.right_side = right_side
    clock = pg.time.Clock()
    #get images
    images = level.load_images(const['window'].WIDTH, const['window'].HEIGHT)
    #zabky
    numbers = level.right_side
    frogs = []
    for i in range(len(numbers)):
        frogs.append(Zabka(numbers[i], pg, 80*i))
    exit_code = -1
    zabiek_na_dreve = 0
    win_animacia = Win(pg, screen)
    lose_animacia = Lose(pg, screen)
    #------HOME BUTTON
    images['back_rect'].topleft = (0,const['window'].HEIGHT-images['back'].get_height())
    #-------HELPING
    level.start_pos = [const['window'].WIDTH-images['q_mark'].get_width(), 0]
    level.act_pos = level.start_pos.copy()

    surface_help = pg.Surface((300,images['q_mark'].get_height()))
    surface_help.set_alpha(128)
    surface_help.fill((0, 149, 255))
    surface_help_rect = surface_help.get_rect()

    text_help_font = pg.font.Font('freesansbold.ttf', 32)
    text_help_surface = text_help_font.render('11 = a + b', True, const['color'].BLACK)
    text_help_rect = text_help_surface.get_rect()
    #--------TEXT
    intro_text, intro_rect = level.generate_text(const['window'].WIDTH, const['color'].BLACK)
    #------------MAIN LOOP
    while True:
        #---------PLACE IMAGES
        #set backgrund image
        screen.blit(images['farm'], (0,0))
        #set text
        screen.blit(intro_text, intro_rect)
        #set log end
        screen.blit(images['log_end'], (const['window'].WIDTH//3-120, 500))
        #set log
        screen.blit(images['log'], (const['window'].WIDTH//3-300, 390))
        #set box
        screen.blit(images['box'], (610, 400))
        #set home
        screen.blit(images['back'], images['back_rect'])
        #HELPING
            #set ask
        images['q_mark_rect'].topleft = level.act_pos
        screen.blit(images['q_mark'], images['q_mark_rect'])
            #rect
        surface_help_rect[0] = level.act_pos[0]
        surface_help_rect[1] = level.act_pos[1]
        screen.blit(surface_help, surface_help_rect)
            #text
        text_help_rect.topleft = (level.act_pos[0] + images['q_mark'].get_width(), 20)
        screen.blit(text_help_surface, text_help_rect)
        #weight
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
                    frog.max = 2
            elif frog.as_rect().collidepoint(mouse_coor):
                frog.active_grp = frog.grp2
                frog.active = 2
            else:
                frog.active_grp = frog.grp1
                frog.active = 1
            frog.kresli_info.draw(screen)
            spolu_na_hojdacke_vaha += frog.na_hojdacke

        if surface_help_rect.collidepoint(mouse_coor):
            if level.act_pos[0] >= level.start_pos[0] - level.max_off:
                level.act_pos[0] -= 6
        else:
            if level.act_pos[0] < level.start_pos[0]:
                level.act_pos[0] += 6

        if images['back_rect'].collidepoint(mouse_coor) and mouse_clicked:
            return 2

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
                if exit_code == 1:
                    win_animacia.animate()
                    if not win_animacia.is_animating:
                        return exit_code
                else:
                    lose_animacia.animate()
                    if not lose_animacia.is_animating:
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
