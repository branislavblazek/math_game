import heapq
import files

class Level:
    def __init__(self, pygame):
        self.pg = pygame
        #for help:
        self.start_pos = [0,0]
        self.max_off = 350
        self.act_pos = self.start_pos
        #for points
        self.point_size = 100
        self.point_full_size = 200
        self.point_rest = self.point_full_size - self.point_size
        self.table_width = 800
        self.table_height = 400
        #system for going
        self.vertex_active = 'A'
        self.vertex_path = ['A']
        self.vrcholy = None
        #for monkey
        self.monkey_width = 150
        self.monkey_height = 190
        self.pos = [0,476]
        self.speed = 10
        self.tole = 5
        self.can_end = False
        self.vynutene_skoncenie = False
        #for path
        self.correct_ans = -1
        self.act_value = 0
        self.done = 0
        self.in_end = False

    def load_images(self):
        anim = files.animation_images.Get_images(self.pg)
        path = 'opicky/resources/'
        images = {
            "jungle": self.pg.image.load(path + 'jungle_blue.png'),
            "back": anim.back,
            "q_mark": anim.q_mark,
            "banana_full": self.pg.image.load(path + 'banana2.png'),
            "banana_null": self.pg.image.load(path + 'banana22.png'),
            "point": self.pg.image.load(path + 'vrchol.png'),
            'point2': self.pg.image.load(path + 'vrchol2.png'),
            'monkey': self.pg.image.load(path + 'monkey_org.png'),
            'lano': self.pg.image.load(path + 'lano.png'),
            'finish': self.pg.image.load(path + 'finish.png')
        }
        images['back_rect'] = images['back'].get_rect()
        images['q_mark_rect'] = images['q_mark'].get_rect()
        images['point'] =  self.pg.transform.scale(images['point'], (self.point_size,self.point_size))
        images['point2'] =  self.pg.transform.scale(images['point2'], (self.point_size,self.point_size))
        images['monkey'] = self.pg.transform.scale(images['monkey'], (self.monkey_width, self.monkey_height))
        images['lano'] = self.pg.transform.scale(images['lano'], (280,158))

        return images

    def create_lana(self):
        #type1 == * *
        #type2 == *
        #         *
        #type3 == *
        #           *
        #type4 ==   *
        #         *
        polohy = {
            'type1': [],
            'type2': [],
            'type3': [],
            'type4': []
        }

        for vrchol in self.vrcholy.items():
            if vrchol[0] == 'A' or vrchol[0] == 'J':
                continue
            
            x1 = vrchol[1].coords[1][0]
            y1 = vrchol[1].coords[1][1]
            
            susedia = vrchol[1].neig
            for sused in susedia:
                if sused == 'A' or sused == 'J':
                    continue

                if vrchol[1].is_connected_with(sused):
                    continue
                else:
                    #1. zisti polohu
                    #print(sused, self.vrcholy[sused].coords[1])
                    x2 = self.vrcholy[sused].coords[1][0]
                    y2 = self.vrcholy[sused].coords[1][1]

                    if y1 == y2:
                        polohy['type1'].append((x1, y1))
                        #print(sused, 'vodorovne')
                    elif x1 == x2:
                        polohy['type2'].append((x1, y1))
                        #print(sused, 'vertikalne')
                    elif x1 < x2:
                        polohy['type3'].append((x1, y1))
                        #print(sused, 'diagonala dole')
                    elif x1 > x2:
                        polohy['type4'].append((x1 - (x1 - x2), y1))
                        #print('diagonala hore')
                    #2. pridaj do zoznamu
                    #print('pridavam' + sused)
                    vrchol[1].connected_with.add(sused)
                    self.vrcholy[sused].connected_with.add(vrchol[0])

        return polohy

    def monkey_coords(self):
        #kolko ich ostava spravit
        task = self.vertex_path[self.done:]
        
        if len(task):
            destination = list(self.vrcholy[task[0]].rect.center)
            if self.pos[0] in range(destination[0]-self.tole, destination[0]+self.tole) and self.pos[1] in range(destination[1]-self.tole, destination[1]+self.tole):
                self.done += 1
                if self.vynutene_skoncenie:
                    self.in_end = True
                if self.vertex_path[-1] == 'J':
                    self.in_end = True
                
            else:
                if self.pos[0] < destination[0]-self.tole and destination[0]:
                    self.pos[0] += self.speed
                elif self.pos[0] > destination[0]+self.tole and destination[0]:
                    self.pos[0] -= self.speed
 
                if self.pos[1] < destination[1]-self.tole and destination[1]:
                    self.pos[1] += self.speed
                elif self.pos[1] > destination[1]+self.tole and destination[1]:
                    self.pos[1] -= self.speed

        if self.vertex_path[-1] == 'J' and len(task) == 0 and self.in_end:
            self.can_end = True
        if len(task) == 0 and self.in_end:
            self.can_end = True

        x = self.pos[0] - (self.monkey_width // 2 + 15)
        y = self.pos[1] - (self.monkey_height // 2 + 60)

        return x, y

    def generate_text(self, text, top, width, color):
        intro_textObj = self.pg.font.SysFont('impact', 46)
        intro_textSurfaceObj = intro_textObj.render(text, True, color)
        intro_textRectObj = intro_textSurfaceObj.get_rect()
        intro_textRectObj.center = (width//2, top)

        return intro_textSurfaceObj, intro_textRectObj

    def dijkstra(self, graf, zac, kon):
        heap = []
        navs = [-1] * len(graf)
        
        heapq.heappush(heap, (0, zac))
        
        while heap:
            x = heapq.heappop(heap)

            vzdial = x[0]
            vrchol = x[1][0]
            
            if(navs[vrchol] != -1):
                continue
            
            navs[vrchol] = vzdial
                
            for i in range(0, len(graf[vrchol])):
                novy_vrchol = graf[vrchol][i]
                
                if(navs[novy_vrchol[0]] == -1):
                    z = (vzdial+graf[vrchol][i][1], novy_vrchol)
                    heapq.heappush(heap, z)

        return navs[kon[0]]

class Point:
    def __init__(self, xy):
        self.top = xy[1]
        self.left = xy[0]
        self.point_size = 100
        self.point_full_size = 200
        self.point_rest = self.point_full_size - self.point_size
        self.image = None
        self.rect = None
        self.neig = None
        self.type = 1
        self.connected_with = set()
        self.value = 0

    @property
    def coords(self):
        return self.image[self.type-1], (self.left, self.top)

    def make_rect(self):
        self.rect = self.image[self.type-1].get_rect()
        self.rect.topleft = (self.left, self.top)

    def is_connected_with(self, pointB):
        if pointB in self.connected_with:
            return True
        else:
            return False

    def generate_number(self):
        return self.value, self.rect.center

class Win:
    def __init__(self, pg, screen):
        self.pg = pg
        self.screen = screen
        self.win = files.animation_images.Get_images(self.pg).right
        self.win_rect = self.win.get_rect()
        self.is_animating = False
        self.w, self.h = self.pg.display.get_surface().get_size()
        self.size = 0

    def animate(self):
        self.is_animating = True
        one_per = self.win.get_size()[0]//100
        new_size = one_per * self.size
        self.size += 2
        transformed = self.pg.transform.scale(self.win, (new_size, new_size))
        self.win_rect = transformed.get_rect()
        self.win_rect.center = (self.w//2, self.h//2)
        if self.size >= 100:
            self.is_animating = False

        self.screen.blit(transformed, self.win_rect)

class Lose:
    def __init__(self, pg, screen):
        self.pg = pg
        self.screen = screen
        self.wrong = files.animation_images.Get_images(self.pg).left
        self.wrong_rect = self.wrong.get_rect()
        self.is_animating = False
        self.w, self.h = self.pg.display.get_surface().get_size()
        self.size = 0

    def animate(self):
        self.is_animating = True

        one_per = self.wrong.get_size()[0]//100
        new_size = one_per * self.size
        self.size += 2
        transformed = self.pg.transform.scale(self.wrong, (new_size, new_size))
        self.wrong_rect = transformed.get_rect()
        self.wrong_rect.center = (self.w//2, self.h//2)
        if self.size >= 100:
            self.is_animating = False

        self.screen.blit(transformed, self.wrong_rect)