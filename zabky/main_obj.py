import random
import files

class Level:
    def __init__(self, status, pygame):
        self.level_status = status
        self.pg = pygame
        self.numbers_left = [10,5,2,1]
        self.left_side = self.get_left_side()
        self.left_side_n = self.left_side
        self.left_side = sum(self.left_side)
        #for help:
        self.start_pos = [0,0]
        self.max_off = 200
        self.act_pos = self.start_pos

    def load_images(self, window_width, window_height):
        anim = files.animation_images.Get_images(self.pg)
        path = 'zabky/resources/'
        images = {
            "farm": self.pg.image.load(path + 'farm.png'),
            "log_end": self.pg.image.load(path + 'log_end.png'),
            "log": self.pg.image.load(path + 'log.png'),
            "box": self.pg.image.load(path + 'box.png'),
            "weight": self.pg.image.load(path + 'weight.png'),
            "star_full": self.pg.image.load(path + 'star_1.png'),
            "star_null": self.pg.image.load(path + 'star_0.png'),
            "back": anim.back,
            "q_mark": anim.q_mark
        }
        images['farm'] = self.pg.transform.scale(images['farm'], (window_width, window_height))
        images['log_end'] = self.pg.transform.scale(images['log_end'], (200, 200))
        images['log'] = self.pg.transform.scale(images['log'], (560,200))
        images['box'] = self.pg.transform.scale(images['box'], (380, 380))
        images['weight'] = self.pg.transform.scale(images['weight'], (180, 200))
        images['back_rect'] = images['back'].get_rect()
        images['q_mark_rect'] = images['q_mark'].get_rect()


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
        return numbers[:cislo]

    def generate_text(self, width, color):
        intro_textObj = self.pg.font.SysFont('impact', 46)
        intro_textSurfaceObj = intro_textObj.render('Ktoré 2 žabky sú potrebné na vyrovnanie?', True, color)
        intro_textRectObj = intro_textSurfaceObj.get_rect()
        intro_textRectObj.center = (width//2,120)
        return intro_textSurfaceObj, intro_textRectObj

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
        self.img2 = self.pg.image.load(path + 'frog2.png')
        self.img2 = self.pg.transform.scale(self.img2, (120, 150))
        self.posun = posun
        #ako kolkata zabka je na hojdacke, nieco ako index
        self.kolkata = -1
        self.max = -1
        self.grp1 = self.make_group(self.img)
        self.grp2 = self.make_group(self.img2)
        self.active_grp = self.grp2
        self.active = 1

    def make_group(self, which_img):
        sprite = self.pg.sprite.Sprite()
        sprite.image = which_img
        sprite.rect = which_img.get_rect()
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
        return group

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

        self.grp1.sprites()[0].rect.left = self.x
        self.grp1.sprites()[0].rect.top = self.y
        self.grp2.sprites()[0].rect.left = self.x
        self.grp2.sprites()[0].rect.top = self.y

        return self.grp1 if self.active == 1 else self.grp2

    def as_rect(self):
        copy_img = self.grp1.sprites()[0].rect
        return copy_img

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
