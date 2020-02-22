class Mascot_animation:
    def __init__(self, coors):
        self.is_showing = False
        self.is_hiding = False
        self.is_showed = False
        self.is_hided = True
        self.starting_coors = coors
        self.actual_coors = self.starting_coors
        self.max_off = 180
        self.speed = 10

    def position(self):
        new_x, new_y = self.actual_coors

        if new_y > self.starting_coors[1]:
            self.is_hiding = False
            self.is_hided = True
            new_y -= self.speed
        elif self.is_hiding == True and self.is_hided == False:
            new_y += self.speed
        elif new_y <= self.starting_coors[1] - self.max_off:
            self.is_showing = False
            self.is_showed = True
        elif self.is_showing == True and self.is_showed == False:
            new_y -= self.speed

        self.actual_coors = new_x, new_y
        return self.actual_coors
