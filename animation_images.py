class Get_images:
    def __init__(self, pg):
        self.pg = pg
        self.right = self.pg.image.load('right.png')
        self.left = self.pg.image.load('wrong.png')
        self.back = self.pg.image.load('back.png')
        self.q_mark = self.pg.image.load('question-mark.png')
