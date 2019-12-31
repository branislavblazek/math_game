class Consts_game:
    def __init__(self):
        self.WIN_WIDTH =  1024
        self.WIN_HEIGHT = 768
        self.WIN_TITLE = 'Zajko usko'
        self.BUNNY_WIDTH = 135
        self.ROCK_TOP_OFFSET = 480
        self.ROCK_NUM = 6
        self.ins_num = 10
        self.ROCK_WIDTH = self.WIN_WIDTH // (self.ROCK_NUM + 1)
        self.rock_height = None

class Consts_colors:
    def __init__(self):
        self.GRAY     = (100, 100, 100)
        self.NAVYBLUE = ( 60,  60, 100)
        self.WHITE    = (255, 255, 255)
        self.RED      = (255,   0,   0)
        self.GREEN    = (  0, 255,   0)
        self.BLUE     = (  0,   0, 255)
        self.YELLOW   = (255, 255,   0)
        self.ORANGE   = (255, 128,   0)
        self.PURPLE   = (255,   0, 255)
        self.CYAN     = (  0, 255, 255)
        self.BLACK    = (  0,   0,   0)
