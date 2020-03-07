import files

class Level:
    def __init__(self, pygame):
        self.pg = pygame
        #for help:
        self.start_pos = [0,0]
        self.max_off = 200
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

    def load_images(self):
        anim = files.animation_images.Get_images(self.pg)
        path = 'opicky/resources/'
        images = {
            "jungle": self.pg.image.load(path + 'jungle.png'),
            "back": anim.back,
            "q_mark": anim.q_mark,
            "banana_full": self.pg.image.load(path + 'banana2.png'),
            "banana_null": self.pg.image.load(path + 'banana22.png'),
            "point": self.pg.image.load(path + 'vrchol.png'),
            'point2': self.pg.image.load(path + 'vrchol2.png'),
            'monkey': self.pg.image.load(path + 'monkey_org.png'),
            'lano': self.pg.image.load(path + 'lano.png')
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

        main_vrcholy = self.vrcholy.copy()
        del main_vrcholy['A']
        del main_vrcholy['J']

        for vrchol in main_vrcholy.items():
            #vrchol[0] - oznacenie, vrchol[1] - objekt
            print(vrchol)

        return polohy

    def monkey_coords(self):
        left, top = self.vrcholy[self.vertex_active].rect.center
        left -= self.monkey_width // 2 + 15
        top -= self.monkey_height // 2 + 60
        return left, top

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

    @property
    def coords(self):
        return self.image[self.type-1], (self.left, self.top)

    def make_rect(self):
        self.rect = self.image[self.type-1].get_rect()
        self.rect.topleft = (self.left, self.top)

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