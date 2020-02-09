import random
import files

class Level:
    def __init__(self, status, pygame):
        #in level_status is number of level
        self.level_status = status
        self.pg = pygame
        #start game
        self.start = False
        #number of first number under first rock
        self.initial_number = random.randint(5,10)
        #start position of bunny
        self.bunny_pos = (-130, 260)
        #max height for jumping bunnny
        self.bunny_jump = 11
        self.bunny_jump_pos = self.bunny_jump
        #if bunny is already jumping
        self.isJumping = False
        #on which index is bunny now
        self.now_on_index = -1
        #where is going to jump
        self.going_to_jump = -1
        #height of rocks (top + h)
        self.h_rocks = None
        #where the bunny should jump
        self.index_rock_jump = -1
        #animation for start
        self.animation_offset = 300
        # for fading in rocks
        self.rock_animation_start = False
        self.rock_animation_offset = self.animation_offset
        # for dafing in numbers
        self.numbers_animation_start = False
        self.numbers_animation_offset = self.animation_offset
        #animation for end
        # for fading out rocks
        self.rock_animation_end = False
        self.rock_animation_pos = 0
        # for fading out numbers
        self.numbers_animation_end = False
        self.numbers_animation_pos = 0
        #index where is mouse
        self.rock_hover_index = -1
        self.rock_hover_height = 20
        self.rock_hover_pos = 0
        #old index where is mouse, used to "back" animation
        self.rock_old_hover_index = -1
        self.rock_old_hover_height = self.rock_hover_height
        self.rock_old_hover_pos = self.rock_old_hover_height
        #values for shaking
        self.shake_width = 10
        self.shake_pos = -self.shake_width
        self.shake_index = -1
        self.shake_count = 0
        #if there is True, level will end
        self.exit = False
        #if this is True, fading out animation is working,
        self.going_off = False
        #done exit animation
        self.rock_animation_end_done = False
        self.numbers_animation_end_done = False
        self.correct = None
        #for help:
        self.start_pos = [0,0]
        self.max_off = 200
        self.act_pos = self.start_pos

    def __repr__(self):
        return self.level_status

    def random_rock_height(self, n, top):
        """
        Returns the array of top offset
        for the rocks.
        """
        rocks_height = []
        for i in range(n):
            rocks_height.append(top + random.randint(0,60))
        self.h_rocks = rocks_height

    def load_images(self, width):
        anim = files.animation_images.Get_images(self.pg)
        path = 'krokovanie/resources/'
        images = {
            "grass": self.pg.image.load(path + 'grass.png'),
            "bunny": self.pg.image.load(path + 'bunny.png'),
            "rock": self.pg.image.load(path + 'rock.png'),
            "arrow_to": self.pg.image.load(path + 'arrow.png'),
            "star_null": self.pg.image.load(path + 'star_0.png'),
            "star_full": self.pg.image.load(path + 'star_1.png'),
            "back": anim.back,
            "q_mark": anim.q_mark
        }
        images['arrow_to'] = self.pg.transform.scale(images['arrow_to'], (90, 90))
        images["arrow_back"] = self.pg.transform.flip(images["arrow_to"], True, False)
        #edit images
        pomer = width / (images["rock"].get_width() / 100)
        new_height = int(images["rock"].get_height() / 100 * pomer)
        images["rock"] = self.pg.transform.scale(images["rock"], (width,new_height))
        images['back_rect'] = images['back'].get_rect()
        images['q_mark_rect'] = images['q_mark'].get_rect()

        return images, new_height

    def generate_text(self, width, color):
        intro_textObj = self.pg.font.SysFont('impact', 46)
        intro_textSurfaceObj = intro_textObj.render('Na ktorý kameň doskáče Zajko?', True, color)
        intro_textRectObj = intro_textSurfaceObj.get_rect()
        intro_textRectObj.center = (width//2,120)
        return intro_textSurfaceObj, intro_textRectObj

    def generate_numbers(self, one_width, color, pocet):
        num_textObj = self.pg.font.SysFont('impact', 52)
        num_surface = []
        num_rect = []
        for i in range(pocet):
            surface = num_textObj.render(str(self.initial_number + i), True, color)
            num_surface.append(surface)
            rect = surface.get_rect()
            width = int(i * one_width + one_width // 2)
            num_rect.append(rect)
            num_rect[-1].center = (width, 700)
        return num_surface, num_rect

    def all_same(self, items):
        return all(x == items[0] for x in items)

    def create_ins(self, base_ins_num, rock_n):
            ins = []
            move_rock = 0
            ins_pocet = base_ins_num
            sign = 1
            ins_number = 0
            while ins_number < ins_pocet:
                new_ins_len = random.randint(1,3)

                if ins_number + new_ins_len > ins_pocet:
                    new_ins_len = ins_pocet - ins_number

                if self.all_same(ins[-3:]) and len(ins[-3:]) == 3 and new_ins_len == 3:
                    new_ins_len -= 1

                if move_rock - new_ins_len < 1 and sign == 0:
                    new_ins_len = move_rock - 1
                elif move_rock + new_ins_len > rock_n and sign == 1:
                    new_ins_len = rock_n - move_rock

                for _ in range(new_ins_len):
                    ins.append(sign)

                if sign == 1:
                    move_rock += new_ins_len
                elif sign == 0:
                    move_rock -= new_ins_len
                sign = 1 - sign
                ins_number += new_ins_len

            if move_rock == 2:
                nahodne = random.randint(1,3)
                if nahodne == 1:
                    indexes = [i for i, x in enumerate(ins) if x == 1]
                    index_delete = random.choice(indexes)
                    del ins[index_delete]
                    base_ins_num -= 1
                elif nahodne == 3:
                    indexes = [i for i, x in enumerate(ins) if x == 0]
                    index_delete = random.choice(indexes)
                    del ins[index_delete]
                    move_rock += 1
            if move_rock == 4:
                if random.randint(0,1):
                    indexes = [i for i, x in enumerate(ins) if x == 0]
                    index_delete = random.choice(indexes)
                    del ins[index_delete]
                    move_rock += 1

            return ins, move_rock

    def getRockAtPixel(self, x, y, width, height):
        for rock in range(len(self.h_rocks)):
            hitBox = self.pg.Rect(rock * width + width, self.h_rocks[rock], width, height)
            if hitBox.collidepoint(x,y):
                return (rock * width + width, self.h_rocks[rock])
        return (None, None)

    def bunny_coors(self):
        if self.isJumping:
            x = self.bunny_pos[0]
            y = self.bunny_pos[1]
            if self.index_rock_jump > -1:
                height = self.h_rocks[self.index_rock_jump]
            else:
                height = 260

            if self.bunny_jump_pos >= -self.bunny_jump:
                neg = -1 if self.bunny_jump_pos < 0 else 1
                y -= int((self.bunny_jump_pos ** 2) * 0.5) * neg
                self.bunny_jump_pos -= 1
                x += 6.2
            elif y + 258 >= height and self.bunny_jump_pos < 0:
                self.bunny_jump_pos = self.bunny_jump
                self.isJumping = False
            elif self.bunny_jump_pos < -self.bunny_jump:
                y += height - 480
            else:
                self.bunny_jump_pos = self.bunny_jump
                self.isJumping = False
            self.bunny_pos = (x, y)
        return self.bunny_pos

    def rocks_coors(self, x, y, index):
        ciste_y = y

        if self.rock_animation_start:
            y += self.rock_animation_offset
            if index == len(self.h_rocks) - 1:
                self.rock_animation_offset -= 10
            if self.rock_animation_offset == 0:
                self.rock_animation_start = False
        elif self.rock_animation_end:
            y += self.rock_animation_pos
            if index == len(self.h_rocks) - 1:
                self.rock_animation_pos += 10
            if self.rock_animation_pos >= self.animation_offset:
                self.rock_animation_end = False
                self.rock_animation_end_done = True
        elif self.rock_hover_index != -1 and index == self.rock_hover_index:
            self.rock_hover_index_backup = self.rock_hover_index
            y = self.h_rocks[self.rock_hover_index] - self.rock_hover_pos
            if self.rock_hover_pos <= self.rock_hover_height:
                self.rock_hover_pos += 3
        elif self.rock_old_hover_index != -1 and self.rock_old_hover_index == index:
            y = self.h_rocks[self.rock_old_hover_index] - self.rock_old_hover_pos
            if self.rock_old_hover_pos >= 0:
                self.rock_old_hover_pos -= 3

        if self.shake_index != -1 and index == self.shake_index:
            if self.shake_count == 0:
                if self.shake_pos <= self.shake_width:
                    x -= (self.shake_width - self.shake_pos)
                    self.shake_pos += 5
                else:
                    self.shake_pos = -self.shake_width
                    self.shake_count += 1
            if self.shake_count == 1:
                if self.shake_pos <= self.shake_width:
                    x += (self.shake_width - self.shake_pos)
                    self.shake_pos += 5
                else:
                    self.shake_pos = -self.shake_width
                    self.shake_count = 0
                    self.shake_index = -1

        if self.rock_animation_end_done:
            return x, ciste_y + self.animation_offset
        return x, y

    def numbers_coors(self, y, is_last):
        ciste_y = y

        if self.numbers_animation_start:
            y = y + self.numbers_animation_offset
            if is_last:
                self.numbers_animation_offset -= 10
            if self.numbers_animation_offset <= 0:
                self.numbers_animation_start = False
        elif self.numbers_animation_end:
            y += self.numbers_animation_pos
            if is_last:
                self.numbers_animation_pos += 10
            if self.numbers_animation_pos >= self.animation_offset:
                self.numbers_animation_end = False
                self.numbers_animation_end_done = True

        if self.numbers_animation_end_done:
            return ciste_y + self.animation_offset
        return y

    def start_anim(self):
        if self.start:
            self.rock_animation_start = True
            self.numbers_animation_start = True
            self.isJumping = True
            self.start = False

    def fade_away(self):
        if not self.going_off:
            self.rock_hover_index = -1
            self.rock_old_hover_index = -1
            self.shake_index = -1
            self.rock_animation_end = True
            self.numbers_animation_end = True
            self.isJumping = True
        else:
            self.going_off = True

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
