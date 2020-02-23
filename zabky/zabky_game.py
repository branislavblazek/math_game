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
    spolu_na_hojdacke_vaha = 0
    #get images
    images = level.load_images(const['window'].WIDTH, const['window'].HEIGHT)
    #zabky
    numbers = level.right_side
    frogs = []
    for i in range(len(numbers)):
        frogs.append(Zabka(numbers[i], pg, 100*i))
    exit_code = -1
    zabiek_na_dreve = 0
    win_animacia = Win(pg, screen)
    lose_animacia = Lose(pg, screen)
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
    medzera = "         " if level.left_side < 10 else "       "
    text_help_surface = text_help_font.render(str(level.left_side) + ' =' + medzera +  '+       ', True, const['color'].BLACK)
    text_help_rect = text_help_surface.get_rect()

    frog_help = images['help_frog']
    frog_help_rect = frog_help.get_rect()
    #--------TEXT
    intro_text, intro_rect = level.generate_text(const['window'].WIDTH, const['color'].BLACK)
    intro_text_shade, intro_text_shade_rect =  level.generate_text(const['window'].WIDTH, const['color'].WHITE)
    intro_text_shade_rect.left -= 4
    #------------MAIN LOOP
    while True:
        #---------PLACE IMAGES
        #set backgrund image
        screen.blit(images['farm'], (0,0))

        #set text
        screen.blit(intro_text_shade, intro_text_shade_rect)
        screen.blit(intro_text, intro_rect)

        #set log end
        screen.blit(images['log_end'], (const['window'].WIDTH//3-120, 460))

        #set log
        uhol = level.log_angle(spolu_na_hojdacke_vaha)
        log = images['log'].copy()
        log = pg.transform.rotozoom(log, uhol, 1)
        start_log_x = const['window'].WIDTH//3-20
        start_log_y = 450
        log_rect = log.get_rect()
        log_rect.center = (start_log_x, start_log_y)

        #log = pg.transform.rotozoom(log, 10, 1)
        screen.blit(log, log_rect)

        #set box
        screen.blit(images['box'], (610, 390))

        #set home
        screen.blit(images['back'], images['back_rect'])

        #HOME
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
        frog_help_rect.topleft = (level.act_pos[0] + images['q_mark'].get_width() + 70, 10)
        screen.blit(frog_help, frog_help_rect)
        frog_help_rect.topleft = (level.act_pos[0] + images['q_mark'].get_width() + 150, 10)
        screen.blit(frog_help, frog_help_rect)
        #weight
        images['weight'].sprites()[0].rect.top = 415 - log_rect.top + 280
        images['weight'].draw(screen)
        #info level
        for star in range(level_max):
            if star < level_status:
                screen.blit(images['star_full'], (star*100+20,25))
            else:
                screen.blit(images['star_null'], (star*100+20,25))
        #vaha na hojdacke
        spolu_na_hojdacke_vaha = 0
        #set frog
        can_collide = True
        for frog in frogs:
            if frog.as_rect().collidepoint(mouse_coor) and mouse_clicked:
                mouse_clicked = False
                if frog.jump_direction == -1:
                    frog.is_jumping = True
                    zabiek_na_dreve += 1
                    frog.kolkata = zabiek_na_dreve
                    frog.max = 2
            elif frog.as_rect().collidepoint(mouse_coor) and can_collide:
                frog.active_grp = frog.grp2
                frog.active = 2
                can_collide = False
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

        if surface_home_rect.collidepoint(mouse_coor):
            surface_home.fill(const['color'].YELLOW)
        else:
            surface_home.fill(const['color'].BLUE)

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
