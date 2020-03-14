class Mascot_animation:
    def __init__(self, coors, x=False):
        self.is_showing = False
        self.is_hiding = False
        self.is_showed = False
        self.is_hided = True
        self.starting_coors = coors
        self.actual_coors = self.starting_coors
        self.max_off = 180
        self.speed = 15
        self.axis_x = x
        self.speed_x = 7
        #self.max_off_x = 450

    def position(self):
        new_x, new_y = self.actual_coors

        if new_y > self.starting_coors[1]:
            self.is_hiding = False
            self.is_hided = True
            new_y -= self.speed

            if self.axis_x: #and self.starting_coors[0] + self.max_off_x >= new_x:
                new_x += self.speed_x

        elif self.is_hiding == True and self.is_hided == False:
            new_y += self.speed

            if self.axis_x: #and self.starting_coors[0] < new_x:
                new_x -= self.speed_x

        elif new_y <= self.starting_coors[1] - self.max_off:
            self.is_showing = False
            self.is_showed = True

        elif self.is_showing == True and self.is_showed == False:
            new_y -= self.speed

            if self.axis_x: #and self.starting_coors[0] + self.max_off_x >= new_x:
                new_x += self.speed_x

        self.actual_coors = new_x, new_y
        return self.actual_coors
