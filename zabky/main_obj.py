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
            "log": self.pg.image.load(path + 'log.png')
        }
        images['farm'] = self.pg.transform.scale(images['farm'], (window_width, window_height))
        images['log_end'] = self.pg.transform.scale(images['log_end'], (150, 150))
        images['log'] = self.pg.transform.scale(images['log'], (320,160))

        return images
