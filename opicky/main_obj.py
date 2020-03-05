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
            'point2': self.pg.image.load(path + 'vrchol2.png')
        }
        images['back_rect'] = images['back'].get_rect()
        images['q_mark_rect'] = images['q_mark'].get_rect()
        images['point'] =  self.pg.transform.scale(images['point'], (self.point_size,self.point_size))
        images['point2'] =  self.pg.transform.scale(images['point2'], (self.point_size,self.point_size))

        return images

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