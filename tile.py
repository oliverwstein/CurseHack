class Tile:
    # Mapping of tile types to their characters and walkability
    tile_types = {
    "corridor": ("\u2591", True),
    "up": ("<", True),
    "down": (">", True),
    "open_door": ("O", True),
    "closed_door": ("0", False),
    "floor": ("\u00B7", True),
    "backdrop": (" ", False),
    "vertical_wall": ("|", False),
    "horizontal_wall": ("-", False),
    "top_left_corner": ("\u250C", False),
    "top_right_corner": ("\u2510", False),
    "bottom_left_corner": ("\u2514", False),
    "bottom_right_corner": ("\u2518", False)
}

    def __init__(self, tile_type):
        if tile_type not in Tile.tile_types:
            raise ValueError(f"Unknown tile type: {tile_type}")
        
        self.char, self.walkable = Tile.tile_types[tile_type]
        self.tile_type = tile_type

class Door(Tile):
    def __init__(self, x, y, side, state = 'closed'):
        if state == 'open':
            super().__init__('open_door')
        else:
            super().__init__('closed_door')
        self.x = x
        self.y = y
        self.connected = False
        self.side = side
        self.state = state
    
    def pos(self):
        return (self.x, self.y)
    
    def open(self):
        self.char, self.walkable = Tile.tile_types['open_door']
        self.state = 'open'

    def close(self):
        self.char, self.walkable = Tile.tile_types['closed_door']
        self.state = 'closed'


class Wall(Tile):
    def __init__(self, x, y, tile_type):
        super().__init__(tile_type)
        self.x = x
        self.y = y
    
    def pos(self):
        return (self.x, self.y)

class Stair(Tile):
    def __init__(self, x, y, tile_type):
        super().__init__(tile_type)
        self.x = x
        self.y = y
        
    def pos(self):
        return (self.x, self.y)
    
