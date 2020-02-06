import random

class Level:
    def __init__(self, status, pygame):
        self.level_status = status
        self.pg = pygame
        self.numbers_left = [10,5,2,1]
        self.left_side = self.get_left_side()
        self.left_side_n = self.left_side
        self.left_side = sum(self.left_side)

    def load_images(self, window_width, window_height):
        path = 'zabky/resources/'
        images = {
            "farm": self.pg.image.load(path + 'farm.png'),
            "log_end": self.pg.image.load(path + 'log_end.png'),
            "log": self.pg.image.load(path + 'log.png'),
            "box": self.pg.image.load(path + 'box.png'),
            "weight": self.pg.image.load(path + 'weight.png'),
            "star_full": self.pg.image.load(path + 'star_1.png'),
            "star_null": self.pg.image.load(path + 'star_0.png')
        }
        images['farm'] = self.pg.transform.scale(images['farm'], (window_width, window_height))
        images['log_end'] = self.pg.transform.scale(images['log_end'], (200, 200))
        images['log'] = self.pg.transform.scale(images['log'], (560,200))
        images['box'] = self.pg.transform.scale(images['box'], (380, 380))
        images['weight'] = self.pg.transform.scale(images['weight'], (180, 200))

        #adding text on weight img
        sprite = self.pg.sprite.Sprite()
        sprite.image = images['weight']
        sprite.rect = images['weight'].get_rect()
        sprite.rect.topleft = (65, 300)
        font = self.pg.font.SysFont('Sans', 50)
        if self.left_side < 10:
            plus = 10
        else:
            plus = 0
        text = font.render(str(self.left_side), True, (0,0,0))
        xxx = self.pg.Rect(65+plus,80,50,50)
        sprite.image.blit(text, xxx)
        group = self.pg.sprite.Group()
        group.add(sprite)
        images['weight'] = group

        return images

    def get_left_side(self):
        numbers = self.numbers_left.copy()
        #dve alebo jedno cislo
        percento = random.randint(0,100)
        #chcem 60percent ze padne dvojka
        cislo = 0
        if percento > 40:
            cislo = 2
        else:
            cislo = 1

        random.shuffle(numbers)
        print(numbers[:cislo])
        return numbers[:cislo]

class Zabka:
    def __init__(self, vaha, pg, posun=0):
        self.pg = pg
        self.vaha = vaha
        self.base_coor = [610+posun, 300]
        self.x = self.base_coor[0]
        self.y = self.base_coor[1]
        self.jump_base = 11
        self.jump_count = self.jump_base
        self.is_jumping = False
        #-1 is left, 1 is right, -1 is default
        self.jump_direction = -1
        #udava ci je alebo nie je na hojdacke
        self.na_hojdacke = 0
        path = 'zabky/resources/'
        self.img = self.pg.image.load(path + 'frog.png')
        self.img = self.pg.transform.scale(self.img, (120, 150))
        self.posun = posun
        #ako kolkata zabka je na hojdacke, nieco ako index
        self.kolkata = -1
        self.max = -1

        sprite = self.pg.sprite.Sprite()
        sprite.image = self.img
        sprite.rect = self.img.get_rect()
        sprite.rect.x = self.x
        sprite.rect.y = self.y
        font = self.pg.font.SysFont('Sans', 40)
        text = font.render(str(self.vaha), True, (0,0,0))

        if self.vaha < 10:
            plus = 10
        else:
            plus = 0

        xxx = self.pg.Rect(40+plus,80,50,50)
        sprite.image.blit(text, xxx)
        group = self.pg.sprite.Group()
        group.add(sprite)
        self.img = group

    @property
    def kresli_info(self):
        if self.is_jumping:
            if self.jump_count >= -self.jump_base:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                posun = self.posun//80
                self.x += (13+posun) * self.jump_direction
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = self.jump_base
                if self.jump_direction == 1:
                    self.na_hojdacke = 0
                    self.jump_direction = -1
                elif self.jump_direction == -1:
                    self.na_hojdacke = self.vaha
                    self.jump_direction = 1
        self.img.sprites()[0].rect.left = self.x
        self.img.sprites()[0].rect.top = self.y
        return self.img

    def as_rect(self):
        copy_img = self.img.sprites()[0].rect
        return copy_img

class Win:
    def __init__(self, pg, screen):
        self.pg = pg
        self.screen = screen
        self.is_animating = False
        self.font_obj = self.pg.font.Font('freesansbold.ttf', 64)
        self.text_surface = self.font_obj.render('You win!', True, (0,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.w, self.h = self.pg.display.get_surface().get_size()
        self.text_rect.center = (self.w//2, -20)
        self.posun = 0

    def animate(self):
        self.is_animating = True
        nove_miesto = self.text_rect.copy()
        self.posun += 2
        nove_miesto.y += self.posun
        self.screen.blit(self.text_surface, self.text_rect)
