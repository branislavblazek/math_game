from opicky.main_obj import Level, Point, Win, Lose
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
    #animations
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
    medzera = "         " if 9 < 10 else "       "
    text_help_surface = text_help_font.render(str(9) + ' =' + medzera +  '+       ', True, const['color'].BLACK)
    text_help_rect = text_help_surface.get_rect()

    #frog_help = images['help_frog']
    #frog_help_rect = frog_help.get_rect()

    #vrcholy
    #   B C D E
    # A         J
    #   F G H I
    vrcholy = {}

    #table
    normal_width = pg.display.Info().current_w
    normal_height = pg.display.Info().current_h
    left = (normal_width - level.table_width) * 0.5
    top = (normal_height - level.table_height) * 0.75

    #pg.draw.rect(screen, const['color'].RED, (left, top, level.table_width, level.table_height), 8)

    pomocne_coord = []
    pomocne_names = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    susedia = (
        ['A', 'B', 'F'],
        ['B', 'A', 'F', 'G', 'C'],
        ['C', 'B', 'F', 'G', 'H', 'D'],
        ['D', 'C', 'G', 'H', 'I', 'E'],
        ['E', 'D', 'H', 'I', 'J'],
        ['F', 'A', 'B', 'C', 'G'],
        ['G', 'F', 'B', 'C', 'D', 'H'],
        ['H', 'G', 'C', 'D', 'E', 'I'],
        ['I', 'H', 'D', 'E', 'J'],
        ['J', 'E', 'I']
    )
    #main points
    for y in range(2):
        for x in range(4):
            pomocne_coord.append((left+level.point_rest/2+level.point_full_size*x, top+level.point_rest/2+level.point_full_size*y))

    for index, name in enumerate(pomocne_names):
        vrcholy[name] = Point(pomocne_coord[index])
        vrcholy[name].image = [images['point'], images['point2']]
        vrcholy[name].make_rect()

    #start point
    left_s = ((left+level.point_rest/2) - level.point_size) / 2
    top = top + (level.table_height - level.point_size) / 2
    vrcholy['A'] = Point((left_s, top))
    vrcholy['A'].image = [images['point'], images['point2']]
    vrcholy['A'].make_rect()
    #end point
    left_e = normal_width - left_s - level.point_size
    vrcholy['J'] = Point((left_e, top))
    vrcholy['J'].image = [images['point'], images['point2']]
    vrcholy['J'].make_rect()
    #neighbours
    for sused in susedia:
        vrcholy[sused[0]].neig = sused[1:]

    #set in level
    level.vrcholy = vrcholy

    coors_lana = level.create_lana()

    #-------MAIN LOOP
    while True:
        #<CHECKING>
        #check for correct image:
        for vrchol in level.vertex_path:
            if vrcholy[vrchol].type != 2:
                vrcholy[vrchol].type = 2

        #check last element
        if level.vertex_path[-1] == 'J':
            print('[~113]The end has come!')
            exit_code = 1

        #check for free neighbours
        pocet = 0
        for sused in vrcholy[level.vertex_active].neig:
            if vrcholy[sused].type == 1:
                pocet += 1
        if pocet == 0:
            print('There is no way!')
            exit_code = 0

        #</CHECKING>

        #<PLACE SOME IMAGES>
        #backgorund image
        screen.blit(images['jungle'], (0,0))

        #home
        surface_home_rect[0] = pg.display.Info().current_w - images['back'].get_width()
        surface_home_rect[1] = pg.display.Info().current_h - images['back'].get_height()
        images['back_rect'][0] = pg.display.Info().current_w - images['back'].get_width()
        images['back_rect'][1] = pg.display.Info().current_h - images['back'].get_height()
        screen.blit(surface_home, surface_home_rect)
        screen.blit(images['back'], images['back_rect'])   

        #helping
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

        #vrcholy:
        for vrchol in vrcholy.items():
            screen.blit(*vrchol[1].coords)

        #lana
        test = images['lano'].copy()
        test = pg.transform.rotozoom(test, -45, 1)
        screen.blit(test, (vrcholy['B'].coords[1][0], vrcholy['B'].coords[1][1]))

        #opicka:
        screen.blit(images['monkey'], level.monkey_coords())
        #</IMAGES PLACING>

        #<MOUSE ACTIONS>
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
            
        #clicked on of the vertex
        if mouse_clicked and mouse_coor != (0,0):
            for vrchol in vrcholy.items():
                if vrchol[1].rect.collidepoint(mouse_coor):
                    mouse_clicked = False
                    if vrchol[0] in vrcholy[level.vertex_active].neig and vrchol[0] not in level.vertex_path:
                        level.vertex_active = vrchol[0] 
                        level.vertex_path.append(level.vertex_active)
                        print(level.vertex_path)
                    break
        #</MOUSE ACTIONS>

        #exiting
        if exit_code == 1 or exit_code == 0:
            can_return = True
            #for frog in frogs:
            #    if frog.is_jumping:
            #        can_return = False

            if can_return:
                if exit_code == 1:
                    win_animacia.animate()
                    if not win_animacia.is_animating:
                        return exit_code
                else:
                    lose_animacia.animate()
                    if not lose_animacia.is_animating:
                        return exit_code

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