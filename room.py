import random
from tile import *
from monster import *
from monster_data import *

class Room:
    """
    The `Room` class represents a single room within a level of the game. It manages the room's dimensions,
    doors, and other features, providing methods to generate and handle these elements.

    Attributes:
        x1, y1 (int): The top-left coordinates of the room.
        width, height (int): The dimensions of the room.
        depth (int): The depth of the room within the dungeon.
        area (int): The total area of the room.
        doors (list): A list of Door objects representing the doors in the room.
        features (list): A list of features present in the room.

    Functions:
        __init__(x1, y1, width, height, depth): Initializes a new room with given dimensions and depth.
        generate_door_on_side(side): Generates a door on a specified side of the room.
        generate_feature(pos, feature): Generates a feature in the room at a specified position.
        get_feature_locations(feature_class): Returns positions of features of a given class within the room.
        get_non_door_adjacent_floor_locations(): Returns floor locations in the room that are not adjacent to doors.

    Usage:
        `Room` objects are used by the `Level` class to create and manage individual rooms within a level. 
        They are key to structuring the dungeon layout and populating it with doors and other features.
    """
    def __init__(self, x1, y1, width, height, depth):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.depth = depth
        self.area = self.width * self.height
        self.doors = []
        self.features = []

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

    def generate_feature(self, pos=None, feature=None):
        # Generate a position if not provided, ensuring it doesn't block a door
        if pos is None:
            pos = self.random_spot(self.get_non_door_adjacent_floor_locations())

        # Create the Feature object with the provided or randomly chosen feature
        new_feature = Feature(*pos, feature)

        # Append the created feature to the room's features
        room.features.append(new_feature)
        
    def get_feature_locations(self, feature_class):
        # List to store positions of features of the given class
        feature_positions = []

        # Iterate through the room's features
        for feature in self.features:
            # Check if the feature is an instance of the specified class
            if isinstance(feature[1], feature_class):
                # Append the position of the feature to the list
                feature_positions.append(feature[0])

        return feature_positions

    def get_non_door_adjacent_floor_locations(self):
        door_locations = self.get_feature_locations(Door)
        floor_locations = self.get_feature_locations(Floor)

        # Generate positions adjacent to doors
        adjacent_to_doors = set()
        for x, y in door_locations:
            adjacent_to_doors.update({(x-1, y), (x+1, y), (x, y-1), (x, y+1)})

        # Filter out floor locations that are adjacent to doors
        non_adjacent_floor_locations = [pos for pos in floor_locations if pos not in adjacent_to_doors]

        return non_adjacent_floor_locations

    def random_spot(self, options=[]):
        # If the list of options is empty, pick a random floor tile
        if not options:
            options = self.get_feature_locations(Floor)
        
        # Check if options list is still empty after trying to get floor locations
        if not options:
            raise ValueError("No available spots to choose from.")

        # Return a random tuple from options
        return random.choice(options)

    def generate_monster(self, pos = None, monster = None):
        #TODO
        pass