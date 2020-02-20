class Get_images:
    def __init__(self, pg):
        self.pg = pg
        self.right = self.pg.image.load('resources/right.png')
        self.left = self.pg.image.load('resources/wrong.png')
        self.back = self.pg.image.load('resources/back.png')
        self.q_mark = self.pg.image.load('resources/question-mark.png')
