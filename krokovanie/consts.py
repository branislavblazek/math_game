import sys
sys.path.insert(0, "..")

import files
window_inf = files.window.Consts_window()

class Consts_game:
    def __init__(self):
        self.BUNNY_WIDTH = 135
        self.ROCK_TOP_OFFSET = 480
        self.ROCK_NUM = 6
        self.ins_num = 8
        self.ROCK_WIDTH = window_inf.WIDTH // (self.ROCK_NUM + 1)
        self.rock_height = None
