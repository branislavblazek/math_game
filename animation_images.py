class Get_images:
    def __init__(self, pg):
        self.pg = pg
        self.right = self.pg.image.load('right.png')
        self.left = self.pg.image.load('wrong.png')
