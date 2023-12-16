import random
from feature import Feature
from tile import Tile, Door, Wall, Stair

class Room:
    def __init__(self, x1, y1, width, height, features = [], gens = [], lit = False):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.features = features
        self.gens = gens
        self.lit = lit
        self.doors = []

    def generate_door_on_side(self, side):
        if side == 'top':
            x = random.randint(self.x1 + 1, self.x1 + self.width - 2)
            y = self.y1
        elif side == 'bottom':
            x = random.randint(self.x1 + 1, self.x1 + self.width - 2)
            y = self.y1 + self.height - 1
        elif side == 'left':
            x = self.x1
            y = random.randint(self.y1 + 1, self.y1 + self.height - 2)
        elif side == 'right':
            x = self.x1 + self.width - 1
            y = random.randint(self.y1 + 1, self.y1 + self.height - 2)
        else:
            raise ValueError("Invalid side specified")

        # Create a Door object
        return Door(x, y, side)

    def place_feature(self, feature, x, y):
        pass
