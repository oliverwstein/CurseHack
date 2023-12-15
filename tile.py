class Tile:
    # Mapping of tile types to their characters and walkability
    tile_types = {
    "corridor": ("#", True),
    "up_stair": ("<", True),
    "down_stair": (">", True),
    "open_door": ("\u22EE", True),
    "closed_door": ("\u2718", False),
    "floor": ("\u00B7", True),
    "backdrop": ("\u2591", False),
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



