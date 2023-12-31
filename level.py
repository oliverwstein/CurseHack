import curses
import random
from tile import *
import kruskal
from room import Room
from feature import Feature
from monster import *
from monster_data import *

class Level():
    """
    The `Level` class is responsible for creating and managing the layout of each level in the game.
    It handles the generation of rooms, corridors, features, and the overall structure of the level.

    Attributes:
        width (int): The width of the level.
        height (int): The height of the level.
        area (int): The total area of the level.
        room_threshold (int): The threshold for the number of rooms in the level.
        depth (int): The depth of the level in the dungeon.
        rooms_placed (list): A list of rooms that have been placed in the level.
        grid (list): A 2D grid representing the level layout.

    Functions:
        __init__(width, height, room_threshold, depth): Initializes a new level with given dimensions and parameters.
        tile_room(room): Tiles a given room within the level.
        create_grid(): Creates the initial grid for the level.
        render(stdscr): Renders the level on the given Curses standard screen.
        add_room(): Attempts to add a new room to the level.
        is_valid_room_placement(new_room, buffer): Checks if a room can be placed without overlapping existing rooms.
        sort_rooms(): Sorts the placed rooms based on their position.
        generate_corridor(start, end, max_corridor_length): Generates a corridor between two points.
        add_doors(): Adds doors to the rooms in the level.
        calculate_room_distances(): Calculates distances between rooms for corridor generation.
        add_corridors(max_corridor_length): Adds corridors to connect the rooms using a minimum spanning tree algorithm.
        add_corridor_to_grid(corridor): Adds a generated corridor to the level grid.
        add_stairs(): Adds stairs to the level for transitioning between levels.
        add_feature(room, pos, feature): Adds a feature to a specified room in the level.

    Usage:
        A `Level` object is created for each level of the dungeon. It is used to generate the layout,
        place rooms and corridors, and manage the features within the level.
    """
    def __init__(self, width, height, room_threshold, depth):
        self.width = width
        self.height = height
        self.area = width*height
        self.room_threshold = room_threshold
        self.depth = depth
        self.rooms_placed = []
        self.grid = self.create_grid()
        self.monsters = []


    def tile_room(self, room):
        for i in range(room.x1, room.x1 + room.width):
            for j in range(room.y1, room.y1 + room.height):
                if 0 <= j < self.height and 0 <= i < self.width:
                    self.grid[i][j] = Floor(i, j, "floor")

                    if j == room.y1:
                        self.grid[i][j] = Wall(i, j, "horizontal_wall")
                    elif j == room.y1 + room.height - 1:
                        self.grid[i][j] = Wall(i, j, "horizontal_wall")
                    if i == room.x1 or i == room.x1 + room.width - 1:
                        self.grid[i][j] = Wall(i, j, "vertical_wall")

                    if (i, j) == (room.x1, room.y1):
                        self.grid[i][j] = Wall(i, j, "top_left_corner")
                    elif (i, j) == (room.x1 + room.width - 1, room.y1):
                        self.grid[i][j] = Wall(i, j, "top_right_corner")
                    elif (i, j) == (room.x1, room.y1 + room.height - 1):
                        self.grid[i][j] = Wall(i, j, "bottom_left_corner")
                    elif (i, j) == (room.x1 + room.width - 1, room.y1 + room.height - 1):
                        self.grid[i][j] = Wall(i, j, "bottom_right_corner")
                    room.features.append([(i, j), self.grid[i][j]])

    def create_grid(self):
        return [[Tile(x, y, "backdrop") for y in range(self.height)] for x in range(self.width)]

    def render(self, stdscr):
        max_y, max_x = stdscr.getmaxyx()

        start_y = max(0, (max_y - self.width) // 2)
        start_x = max(0, (max_x - self.height) // 2)

        for x, column in enumerate(self.grid):
            for y, char in enumerate(column):
                pos_x = start_x + y
                pos_y = start_y + x

                if 0 <= pos_y < max_y and 0 <= pos_x < max_x:
                    stdscr.addch(pos_y, pos_x, char)

        stdscr.refresh()

    def add_room(self):
        attempts = 0
        while attempts < 100:
            width = random.randint(5, 10)
            height = random.randint(5, 8)
            x1 = random.randint(1, self.width - width - 1)
            y1 = random.randint(1, self.height - height - 1)
            
            room = Room(x1, y1, width, height, self.depth)
            if self.is_valid_room_placement(room):
                self.rooms_placed.append(room)
                self.tile_room(room)
                return True
        return False
        
    def is_valid_room_placement(self, new_room, buffer = 3):
        for room in self.rooms_placed:
            if (new_room.x1 < room.x1 + room.width + buffer and
                    new_room.x1 + new_room.width + buffer > room.x1 and
                    new_room.y1 < room.y1 + room.height + buffer and
                    new_room.y1 + new_room.height + buffer > room.y1):
                # Rooms are too close
                return False
        # No overlap with any existing Room
        return True

    def sort_rooms(self):
        self.rooms_placed = sorted(self.rooms_placed, key=lambda room: (room.x1, room.y1))

    def generate_corridor(self, start, end, max_corridor_length):
        corridor_path = []
        x, y = start
        target_x, target_y = end

        while (x, y) != (target_x, target_y):
            # Determine the direction of movement (horizontal or vertical)
            move_horizontally = random.choice([True, False])

            # Determine next step
            if move_horizontally and x != target_x:
                step = 1 if x < target_x else -1
                x += step
            elif not move_horizontally and y != target_y:
                step = 1 if y < target_y else -1
                y += step
            else:
                if x != target_x:
                    step = 1 if x < target_x else -1
                    x += step
                elif y != target_y:
                    step = 1 if y < target_y else -1
                    y += step

            # Check if the next step is the end position
            if (x, y) == (target_x, target_y):
                break

            # Check if the corridor path length exceeds the maximum length
            if len(corridor_path) >= max_corridor_length:
                return False

            # Check if the corridor overlaps with non-backdrop tiles
            if self.grid[x][y].symbol != Tile.tile_types['backdrop'][0]:
                return False

            corridor_path.append((x, y))

        return corridor_path

    def add_doors(self):
        for room in self.rooms_placed:
            for side in ['top', 'bottom', 'left', 'right']:
                door = room.generate_door_on_side(side)
                room.doors.append(door)
                x, y = door.pos
                self.grid[x][y] = door
                room.features.append([door.pos, door])

    def calculate_room_distances(self):
        rooms = self.rooms_placed
        room_distances = {}  # {(room_i_id, room_j_id): (door_i, door_j, distance, corridor)}

        for i, room_i in enumerate(rooms):
            for j, room_j in enumerate(rooms):
                if i != j:
                    shortest_distance = None
                    shortest_corridor = None
                    best_doors = None

                    for door_i in room_i.doors:
                        for door_j in room_j.doors:
                            if not door_i.connected and not door_j.connected:
                                corridor = self.generate_corridor(door_i.pos, door_j.pos, 1000)
                                if corridor:
                                    distance = len(corridor)
                                    if shortest_distance is None or distance < shortest_distance:
                                        shortest_distance = distance
                                        shortest_corridor = corridor
                                        best_doors = (door_i, door_j)

                    if best_doors:
                        room_distances[(i, j)] = best_doors + (shortest_distance, shortest_corridor)

        return room_distances

    def add_corridors(self, max_corridor_length=15):
        uf = kruskal.UnionFind(len(self.rooms_placed))
        room_distances = self.calculate_room_distances()
        sorted_distances = sorted(room_distances.items(), key=lambda x: x[1][2])

        # Track connected rooms
        connected_rooms = set()

        # Adding MST corridors
        for (room_i_id, room_j_id), (door_i, door_j, _, corridor) in sorted_distances:
            if uf.find(room_i_id) != uf.find(room_j_id):
                uf.union(room_i_id, room_j_id)
                connected_rooms.add((min(room_i_id, room_j_id), max(room_i_id, room_j_id)))
                self.add_corridor_to_grid(corridor)
                door_i.connected = True
                door_j.connected = True

        for room in self.rooms_placed:
            for door in room.doors:
                if not door.connected:
                    x, y = door.pos
                    if door.side in ['top', 'bottom']:
                        self.grid[x][y] = Wall(x, y, 'horizontal_wall')
                    elif door.side in ['left']:
                        self.grid[x][y] = Wall(x, y, 'vertical_wall')
                    elif door.side in ['right']:
                        self.grid[x][y] = Wall(x, y, 'vertical_wall')

    def add_corridor_to_grid(self, corridor):
        for x, y in corridor:
            self.grid[x][y] = Tile(x, y, 'corridor')
    
    def add_stairs(self):
        if len(self.rooms_placed) < 2:
            raise ValueError("Not enough rooms to place stairs")

        # Choose two different rooms randomly
        up_stair_room, down_stair_room = random.sample(self.rooms_placed, 2)

        # Place an up-stair in a random tile in one room
        up_stair_x = random.randint(up_stair_room.x1 + 1, up_stair_room.x1 + up_stair_room.width - 2)
        up_stair_y = random.randint(up_stair_room.y1 + 1, up_stair_room.y1 + up_stair_room.height - 2)
        self.grid[up_stair_x][up_stair_y] = Stair(up_stair_x, up_stair_y, 'up')
        self.up_stair = self.grid[up_stair_x][up_stair_y]
        up_stair_room.features.append([(up_stair_x, up_stair_y), self.up_stair])

        # Place a down-stair in a random tile in another room
        down_stair_x = random.randint(down_stair_room.x1 + 1, down_stair_room.x1 + down_stair_room.width - 2)
        down_stair_y = random.randint(down_stair_room.y1 + 1, down_stair_room.y1 + down_stair_room.height - 2)
        self.grid[down_stair_x][down_stair_y] = Stair(down_stair_x, down_stair_y, 'down')
        self.down_stair = self.grid[down_stair_x][down_stair_y]
        down_stair_room.features.append([(down_stair_x, down_stair_y), self.down_stair])
        
    def add_feature(self, room:Room, pos=None, feature=None):
        # If pos is not specified, pick a random spot not adjacent to doors
        if pos is None:
            non_adjacent_floor_locations = room.get_non_door_adjacent_floor_locations()
            if non_adjacent_floor_locations:
                pos = random.choice(non_adjacent_floor_locations)
                
            else:
                #No suitable position found for feature placement
                raise ValueError(f'{len(room.get_feature_locations(Floor))}')

        # If feature is specified but pos is not, update the position of the feature
        if feature is not None and pos is not None:
            feature.pos = pos
        else:
            # If feature is not specified, create it using the generated pos
            feature = Feature(*pos)

        # Append the created or updated feature to the room's features
        room.features.append(feature)
        self.grid[pos[0]][pos[1]] = feature.tile
        return feature

    def generate_monsters(self, feature:Feature, pos = None, mon = None, count = 1):

        if pos is None:
            pos = feature.pos
        if mon == None:
            lured_monsters = set()
            for lure in feature.feature_info['lures']:
                for monster in MonsterData.monsters:
                    if lure in MonsterData.monsters[monster]['traits']:
                        lured_monsters.add(monster)

            mon = Monster.random_monster_based_on_rarity(lured_monsters)

        # Get the data for the chosen monster
        monster_data = MonsterData.monsters[mon]

        monsters = []
        # Check if the monster's "geno" attribute contains the "G_SGROUP" flag
        if "G_SGROUP" in monster_data["geno"]:
            count = random.randint(1, 3)
        nearby_tiles = self.get_nearby_tiles(pos = pos, radius = 2, type = Floor)

        if len(nearby_tiles) <= count:
                chosen_tiles = nearby_tiles
        chosen_tiles = random.sample(nearby_tiles, count)
        # Generate a monster with the "mon" name in each tile
        for tile in chosen_tiles:
            monsters.append(Monster(*tile.pos, mon))

        return monsters
    
    def get_nearby_tiles(self, pos:tuple, radius:int, type:Tile):
        """Return a list of the tiles of Tile subclass tyle 
        within radius of pos."""
        nearby_tiles = []
        x_center, y_center = pos

        # Iterate through each tile within the radius
        for x in range(x_center - radius, x_center + radius + 1):
            for y in range(y_center - radius, y_center + radius + 1):
                # Check if the tile is within the bounds of the map
                if 0 <= x < self.width and 0 <= y < self.height:
                    tile = self.grid[x][y]
                    # Check if the tile is an instance of the specified Tile subclass
                    if isinstance(tile, type):
                        nearby_tiles.append(tile)

        return nearby_tiles




def generate_level(map_width, map_height, room_threshold, depth):

    level = Level(map_width, map_height, room_threshold, depth)
    space = True
    while space:
        if len(level.rooms_placed) >= level.room_threshold:
            break
        level.add_room()
    level.add_doors()
    level.add_corridors()
    level.add_stairs()
    for room in level.rooms_placed:
        feature = level.add_feature(room)
        if random.choice([True, False]):
            level.monsters += level.generate_monsters(feature)
    return level


