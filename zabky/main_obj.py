import random

class Level:
    def __init__(self, status, pygame):
        self.level_status = status
        self.pg = pygame

    def load_images(self, window_width, window_height):
        images = {
            "farm": self.pg.image.load('resources/farm.png'),
            "log_end": self.pg.image.load('resources/log_end.png'),
            "log": self.pg.image.load('resources/log.png')
        }
        images['farm'] = self.pg.transform.scale(images['farm'], (window_width, window_height))
        images['log_end'] = self.pg.transform.scale(images['log_end'], (170,170))

        return images
