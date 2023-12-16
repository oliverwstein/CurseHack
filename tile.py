class Tile:
    # Mapping of tile types to their characters and walkability
    tile_types = {
        "corridor": ("\u2591", True),
        "up": ("<", True),
        "down": (">", True),
        "open_door": ("☖", True),
        "closed_door": ("☗", False),
        "floor": ("\u00B7", True),
        "backdrop": (" ", False),
        "vertical_wall": ("║", False),
        "horizontal_wall": ("═", False),
        "top_left_corner": ("╔", False),
        "top_right_corner": ("╗", False),
        "bottom_left_corner": ("╚", False),
        "bottom_right_corner": ("╝", False),
        "water": ("≈", False),
        "veg": ("ꕥ", True),
        "hot_spring": ("♨", False),
        "rock": ("⭓", False),
    }

    def __init__(self, x, y, tile_type):
        if tile_type not in Tile.tile_types:
            raise ValueError(f"Unknown tile type: {tile_type}")
        self._x = x
        self._y = y
        self.char, self.walkable = Tile.tile_types[tile_type]
        self.tile_type = tile_type

    @property
    def pos(self):
        return (self._x, self._y)

    @pos.setter
    def pos(self, xy):
        if not isinstance(xy, tuple) or len(xy) != 2:
            raise ValueError("Position must be a tuple of two elements: (x, y)")
        self._x, self._y = xy

class Door(Tile):
    def __init__(self, x, y, side, state = 'closed'):
        if state == 'open':
            super().__init__(x, y, 'open_door')
        else:
            super().__init__(x, y, 'closed_door')
        self.connected = False
        self.side = side
        self.state = state
    
    def open(self):
        self.char, self.walkable = Tile.tile_types['open_door']
        self.state = 'open'

    def close(self):
        self.char, self.walkable = Tile.tile_types['closed_door']
        self.state = 'closed'


class Wall(Tile):
    def __init__(self, x, y, tile_type):
        super().__init__(x, y, tile_type)


class Stair(Tile):
    def __init__(self, x, y, tile_type):
        super().__init__(x, y, tile_type)


class Water(Tile):
    def __init__(self, x, y, waterdepth, variant = 'pool', tile_type = 'water'):
        super().__init__(x, y, tile_type)
        self.variant = variant
        if waterdepth == 'Deep':
            self.walkable == False
        else:
            self.walkable == True


class Veg(Tile):
    def __init__(self, x, y, variant = 'moss', tile_type = 'veg'):
        super().__init__(x, y, tile_type)
        self.variant = variant


class Rock(Tile):
    def __init__(self, x, y, tile_type = 'rock'):
        super().__init__(x, y, tile_type)


