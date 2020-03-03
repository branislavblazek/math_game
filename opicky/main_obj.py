import files

class Level:
    def __init__(self, pygame):
        self.pg = pygame
        #for help:
        self.start_pos = [0,0]
        self.max_off = 200
        self.act_pos = self.start_pos

    def load_images(self):
        anim = files.animation_images.Get_images(self.pg)
        path = 'opicky/resources/'
        images = {
            "jungle": self.pg.image.load(path + 'jungle.png'),
            "back": anim.back,
            "q_mark": anim.q_mark,
            "banana_full": self.pg.image.load(path + 'banana2.png'),
            "banana_null": self.pg.image.load(path + 'banana22.png')
        }
        images['back_rect'] = images['back'].get_rect()
        images['q_mark_rect'] = images['q_mark'].get_rect()

        return images