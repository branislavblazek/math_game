from opicky.main_obj import Level, Point, Win, Lose
from opicky.opicky_connections import all_connections
from pygame.locals import *
import sys
import random

#import from sibling folder
sys.path.insert(0, "..")
import files

#initialize the constats
const = {}
const['game'] = None
const['color'] = files.colors.Consts_colors()
const['window'] = files.window.Consts_window()

def opicky_level(pg, screen, level_status, level_max, index):
    clock = pg.time.Clock()
    level = Level(pg)
    #actions
    mouse_clicked = False
    mouse_coor = (0,0)
    #get images
    images = level.load_images()
    #get connections
    getted_connection = all_connections()
    getted_connection = getted_connection[index]
    #exit
    exit_code = -1
    #animations
    win_animacia = Win(pg, screen)
    lose_animacia = Lose(pg, screen)
    #--------TEXT
    intro_text, intro_rect = level.generate_text('Nájdi cestu s najmenším súčtom čísel.', 160, const['window'].WIDTH, const['color'].BLACK)
    intro_text_shade, intro_text_shade_rect = level.generate_text('Nájdi cestu s najmenším súčtom čísel.', 160,const['window'].WIDTH, const['color'].WHITE)
    intro_text_shade_rect.left -= 4

    intro_text2, intro_rect2 = level.generate_text('Na skočené vrcholy nemôžeš skočiť znova!', 220, const['window'].WIDTH, const['color'].BLACK)
    intro_text_shade2, intro_text_shade_rect2 =  level.generate_text('Na skočené vrcholy nemôžeš skočiť znova!', 220, const['window'].WIDTH, const['color'].WHITE)
    intro_text_shade_rect2.left -= 4

    #-------HOME BUTTON
    images['back_rect'].topleft = (0,pg.display.Info().current_h-images['back'].get_height())

    surface_home = pg.Surface((images['back'].get_width(), images['back'].get_height()))
    surface_home.set_alpha(128)
    surface_home.fill((0, 149, 255))
    surface_home_rect = surface_home.get_rect()
    
    #-------HELPING
    level.start_pos = [const['window'].WIDTH-images['q_mark'].get_width(), 0]
    level.act_pos = level.start_pos.copy()

    surface_help = pg.Surface((600,images['q_mark'].get_height()))
    surface_help.set_alpha(128)
    surface_help.fill((0, 149, 255))
    surface_help_rect = surface_help.get_rect()

    text_help_font = pg.font.Font('freesansbold.ttf', 32)
    text_help_surface = text_help_font.render("Zatiaľ získaných: " + str(level.act_value), True, const['color'].BLACK)
    text_help_rect = text_help_surface.get_rect()

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
    #toto susedia_full je nepotrebne
    susedia_full = (
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
    connections = getted_connection
    susedia = []
    for connection in connections:
        start, to = connection.split(' ')

        pridajA = True
        pridajB = True

        for item in susedia:
            if item[0] == start:
                pridajA = False
                item.append(to)
            if item[0] == to:
                pridajB = False
                item.append(start)

        if pridajA:
            susedia.append([start, to])
        if pridajB:
            susedia.append([to, start])

    #main points
    for y in range(2):
        for x in range(4):
            pomocne_coord.append((left+level.point_rest/2+level.point_full_size*x, top+level.point_rest/2+level.point_full_size*y))

    for index, name in enumerate(pomocne_names):
        vrcholy[name] = Point(pomocne_coord[index])
        vrcholy[name].image = [images['point'], images['point2']]
        vrcholy[name].make_rect()
        cislo = random.randint(2, 12)
        vrcholy[name].value = cislo

    #edit susedia to use for dijkstra alg
    graf = [ [] for i in range(10)]

    for sused in susedia:
        zaciatocny = sused[0]
        vedla_neho = sused[1:]
        indexy_vedla = []
        for vedla in vedla_neho:
            hodnota = []
            cislo = ord(vedla) - 65
            #nastav kam to ide
            hodnota.append(cislo)
            #nastav hodnotu
            if cislo == 0 or cislo == 9:
                value = 0
            else:
                value = vrcholy[chr(cislo+65)].value

            hodnota.append(value)
            indexy_vedla.append(hodnota)

        graf[ord(zaciatocny)-65] = indexy_vedla

    level.correct_ans = level.dijkstra(graf, [0,0], [9,0])

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
    a_coors = level.vrcholy['A'].left-20, level.vrcholy['A'].top-40
    e_coors = level.vrcholy['E'].left-10, level.vrcholy['E'].top-20
    i_coors = level.vrcholy['I'].left-20, level.vrcholy['I'].top-150

    #lana
    coors_lana = level.create_lana()
    backup = images['lano'].copy()
    lana_images = {
        'type1': backup,
        'type2': pg.transform.rotozoom(backup, 90, 1),
        'type3': pg.transform.rotozoom(backup, -45, 1),
        'type4': pg.transform.rotozoom(backup, -135, 1),
        'type5': pg.transform.scale(backup, (200, 158))
    }
    lana_images['type5'] = pg.transform.rotozoom(lana_images['type5'], -40, 1)
    lana_images['type5_flip'] = pg.transform.flip(lana_images['type5'], False, True)
    lana_images['type6'] = pg.transform.rotozoom(lana_images['type5'], 80, 1)

    #cisla
    cisla_obj = []
    for name, obj in vrcholy.items():
        if name == 'A' or name == 'J':
            continue 
        value, coors = obj.generate_number()
        intro_textObj = pg.font.SysFont('impact', 50)
        intro_textSurfaceObj = intro_textObj.render(str(value), True, const['color'].WHITE)
        intro_textRectObj = intro_textSurfaceObj.get_rect()
        intro_textRectObj.center = coors

        cisla_obj.append([intro_textSurfaceObj, intro_textRectObj])

    #-------MAIN LOOP
    while True:
        #<CHECKING>
        #check for correct image:
        for vrchol in level.vertex_path:
            if vrcholy[vrchol].type != 2:
                vrcholy[vrchol].type = 2

        #check last element
        if level.vertex_path[-1] == 'J':
            if level.act_value == level.correct_ans:
                exit_code = 1
            else:
                exit_code = 0

        #check for free neighbours
        pocet = 0
        for sused in vrcholy[level.vertex_active].neig:
            if vrcholy[sused].type == 1:
                pocet += 1
        if pocet == 0:
            if level.act_value == level.correct_ans:
                exit_code = 1
            else:
                exit_code = 0

        #</CHECKING>

        #<PLACE SOME IMAGES>
        #backgorund image
        screen.blit(images['jungle'], (0,0))

        #set text
        screen.blit(intro_text_shade, intro_text_shade_rect)
        screen.blit(intro_text, intro_rect)
        screen.blit(intro_text_shade2, intro_text_shade_rect2)
        screen.blit(intro_text2, intro_rect2)
        
        #home
        surface_home_rect[0] = pg.display.Info().current_w - images['back'].get_width()
        surface_home_rect[1] = pg.display.Info().current_h - images['back'].get_height()
        images['back_rect'][0] = pg.display.Info().current_w - images['back'].get_width()
        images['back_rect'][1] = pg.display.Info().current_h - images['back'].get_height()
        screen.blit(surface_home, surface_home_rect)
        screen.blit(images['back'], images['back_rect'])   

        #helping
        text_help_surface = text_help_font.render("Zatiaľ získaných: " + str(level.act_value), True, const['color'].BLACK)
        text_help_rect = text_help_surface.get_rect()
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

        #info level
        for star in range(level_max):
            if star < level_status:
                screen.blit(images['banana_full'], (star * 80 + 20, 25))
            else:
                screen.blit(images['banana_null'], (star * 80 + 20, 25))

        #lana
        for types in coors_lana.items():
            if types[0] == 'type1':
                for coor in types[1]:
                    screen.blit(lana_images[types[0]], (coor[0]+5, coor[1]-30))
            elif types[0] == 'type2':
                for coor in types[1]:
                    screen.blit(lana_images[types[0]], (coor[0]-30, coor[1]+5))
            elif types[0] == 'type3':
                for coor in types[1]:
                    screen.blit(lana_images[types[0]], (coor[0], coor[1]))
            elif types[0] == 'type4':
                for coor in types[1]:
                    screen.blit(lana_images[types[0]], (coor[0], coor[1]-15))

        screen.blit(lana_images['type5'], a_coors)
        screen.blit(lana_images['type5_flip'], (a_coors[0], a_coors[1]-80))
        screen.blit(lana_images['type5'], e_coors)
        screen.blit(lana_images['type6'], i_coors)

        #vrcholy:
        for vrchol in vrcholy.items():
            screen.blit(*vrchol[1].coords)

        #cisla:
        for a, b in cisla_obj:
            screen.blit(a, b)

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
                level.act_pos[0] -= 10
        else:
            if level.act_pos[0] < level.start_pos[0]:
                level.act_pos[0] += 15
            
        #clicked on of the vertex
        if mouse_clicked and mouse_coor != (0,0) and exit_code not in (0,1):
            for vrchol in vrcholy.items():
                if vrchol[1].rect.collidepoint(mouse_coor):
                    mouse_clicked = False
                    if vrchol[0] in vrcholy[level.vertex_active].neig and vrchol[0] not in level.vertex_path:
                        level.vertex_active = vrchol[0] 
                        level.vertex_path.append(level.vertex_active)
                        level.act_value += vrchol[1].value
    
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