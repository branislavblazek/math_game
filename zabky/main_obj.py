import random

class Level:
    def __init__(self, status, pygame):
        self.level_status = status
        self.pg = pygame

    def load_images(self, window_width, window_height):
        path = 'zabky/resources/'
        images = {
            "farm": self.pg.image.load(path + 'farm.png'),
            "log_end": self.pg.image.load(path + 'log_end.png'),
            "log": self.pg.image.load(path + 'log.png'),
            "box": self.pg.image.load(path + 'box.png'),
            "weight": self.pg.image.load(path + 'weight.png')
        }
        images['farm'] = self.pg.transform.scale(images['farm'], (window_width, window_height))
        images['log_end'] = self.pg.transform.scale(images['log_end'], (200, 200))
        images['log'] = self.pg.transform.scale(images['log'], (520,200))
        images['box'] = self.pg.transform.scale(images['box'], (360, 360))
        images['weight'] = self.pg.transform.scale(images['weight'], (180, 200))

        #adding text on weight img
        sprite = self.pg.sprite.Sprite()
        sprite.image = images['weight']
        sprite.rect = images['weight'].get_rect()
        sprite.rect.topleft = (65, 300)
        font = self.pg.font.SysFont('Sans', 50)
        text = font.render('21', True, (0,0,0))
        xxx = self.pg.Rect(65,80,50,50)
        sprite.image.blit(text, xxx)
        group = self.pg.sprite.Group()
        group.add(sprite)
        images['weight'] = group

        return images

class Zabka:
    def __init__(self, vaha, pg):
        self.pg = pg
        self.vaha = vaha
        self.index = -1
        self.base_coor = [620, 300]
        self.x = self.base_coor[0]
        self.y = self.base_coor[1]
        self.jump_base = 11
        self.jump_count = self.jump_base
        self.is_jumping = False
        #-1 is left, 1 is right, -1 is default
        self.jump_direction = -1
        self.na_hojdacke = 0
        path = 'zabky/resources/'
        self.img = self.pg.image.load(path + 'frog.png')
        self.img = self.pg.transform.scale(self.img, (120, 150))

        sprite = self.pg.sprite.Sprite()
        sprite.image = self.img
        sprite.rect = self.img.get_rect()
        sprite.rect.x = self.x
        sprite.rect.y = self.y
        font = self.pg.font.SysFont('Sans', 40)
        text = font.render(str(self.vaha), True, (0,0,0))
        xxx = self.pg.Rect(40,80,50,50)
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
                self.x += 13 * self.jump_direction
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
        self.img.sprites()[self.index].rect.left = self.x
        self.img.sprites()[self.index].rect.top = self.y
        return self.img

    def as_rect(self, index):
        self.index = index
        copy_img = self.img.sprites()[index].rect
        return copy_img
