import random
"""
There is written the main object.
This object will return True is user clicked on good rock.
"""

class Level:
    def __init__(self, status):
        #in level_status is number of level
        self.level_status = status

    def __repr__(self):
        return self.level_status

    def random_rock_height(self, n, top):
        """
        Returns the array of top offset
        for the rocks.
        """
        h_rocks = []
        for _ in range(n):
            h_rocks.append(top + random.randint(0,80))
        return h_rocks
