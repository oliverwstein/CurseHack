import curses
import random
from tile import Tile
import kruskal


class Room:
    def __init__(self, x1, y1, width, height):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.area = self.width * self.height
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

        # Create a Door object with the coordinates and default to 'closed_door' type
        return Door(x, y, side, 'closed_door')


class Door(Tile):
    def __init__(self, x, y, side, tile_type='closed_door'):
        super().__init__(tile_type)
        self.x = x
        self.y = y
        self.connected = False
        self.side = side
    
    def pos(self):
        return (self.x, self.y)

class Wall(Tile):
    def __init__(self, x, y, tile_type):
        super().__init__(tile_type)
        self.x = x
        self.y = y
    
    def pos(self):
        return (self.x, self.y)    

class Level():

    def __init__(self, width, height, room_threshold, depth):
        self.width = width
        self.height = height
        self.area = width*height
        self.room_threshold = room_threshold
        self.depth = depth
        self.rooms_placed = []
        self.grid = self.create_grid()


    def tile_room(self, room):
        for i in range(room.x1, room.x1 + room.width):
            for j in range(room.y1, room.y1 + room.height):
                if 0 <= i < self.width and 0 <= j < self.height:
                    self.grid[j][i] = Tile("floor")

                    # Check if it's an edge and update the character accordingly
                    if i == room.x1 or i == room.x1 + room.width - 1:
                        self.grid[j][i] = Wall(i, j, "vertical_wall")
                    if j == room.y1 or j == room.y1 + room.height - 1:
                        self.grid[j][i] = Wall(i, j, "horizontal_wall")

                    # Check if it's a corner and update the character accordingly
                    if (i, j) == (room.x1, room.y1):
                        self.grid[j][i] = Wall(i, j, "top_left_corner")
                    elif (i, j) == (room.x1 + room.width - 1, room.y1):
                        self.grid[j][i] = Wall(i, j, "top_right_corner")
                    elif (i, j) == (room.x1, room.y1 + room.height - 1):
                        self.grid[j][i] = Wall(i, j, "bottom_left_corner")
                    elif (i, j) == (room.x1 + room.width - 1, room.y1 + room.height - 1):
                        self.grid[j][i] = Wall(i, j, "bottom_right_corner")


    def create_grid(self):
        return [[Tile("backdrop") for _ in range(self.width)] for _ in range(self.height)]


    def render(self, stdscr):
        max_y, max_x = stdscr.getmaxyx()

        # Calculate the position to center the grid
        start_y = max(0, (max_y - len(self.grid)) // 2)
        start_x = max(0, (max_x - len(self.grid[0])) // 2)

        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                # Offset the position to center the grid
                pos_y = start_y + y
                pos_x = start_x + x

                if 0 <= pos_x < max_x and 0 <= pos_y < max_y:
                    stdscr.addch(pos_y, pos_x, char)

        stdscr.refresh()


    def addRoom(self):
        attempts = 0
        while attempts < 100:
            width = random.randint(5, 10)
            height = random.randint(5, 8)
            x1 = random.randint(1, self.width - width - 1)
            y1 = random.randint(1, self.height - height - 1)
            room = Room(x1, y1, width, height)
            if self.is_valid_placement(room):
                self.rooms_placed.append(room)
                self.tile_room(room)
                return True
        return False
        

    def is_valid_placement(self, new_room, buffer = 3):
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
            if self.grid[y][x].char != Tile.tile_types['backdrop'][0]:
                return False

            corridor_path.append((x, y))

        return corridor_path


    def add_doors(self):
        for room in self.rooms_placed:
            for side in ['top', 'bottom', 'left', 'right']:
                door = room.generate_door_on_side(side)
                room.doors.append(door)
                self.grid[door.y][door.x] = door
    

    def calculate_distance(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)
    

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
                                corridor = self.generate_corridor(door_i.pos(), door_j.pos(), 1000)
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
                    if door.side in ['top', 'bottom']:
                        self.grid[door.y][door.x] = Wall(door.x, door.y, 'horizontal_wall')
                    else:
                        self.grid[door.y][door.x] = Wall(door.x, door.y, 'vertical_wall')

    def add_corridor_to_grid(self, corridor):
        for x, y in corridor:
            self.grid[y][x] = Tile('corridor')
    

    def add_stairs(self):
        if len(self.rooms_placed) < 2:
            raise ValueError("Not enough rooms to place stairs")

        # Choose two different rooms randomly
        up_stair_room, down_stair_room = random.sample(self.rooms_placed, 2)

        # Place an up-stair in a random tile in one room
        up_stair_x = random.randint(up_stair_room.x1 + 1, up_stair_room.x1 + up_stair_room.width - 2)
        up_stair_y = random.randint(up_stair_room.y1 + 1, up_stair_room.y1 + up_stair_room.height - 2)
        self.grid[up_stair_y][up_stair_x] = Tile('up_stair')
        self.up_stair = (up_stair_x, up_stair_y)

        # Place a down-stair in a random tile in another room
        down_stair_x = random.randint(down_stair_room.x1 + 1, down_stair_room.x1 + down_stair_room.width - 2)
        down_stair_y = random.randint(down_stair_room.y1 + 1, down_stair_room.y1 + down_stair_room.height - 2)
        self.grid[down_stair_y][down_stair_x] = Tile('down_stair')
        self.down_stair = (down_stair_x, down_stair_y)
        

def generate_level(map_width, map_height, room_threshold, depth):

    level = Level(map_width, map_height, room_threshold, depth)
    space = True
    while space:
        if len(level.rooms_placed) >= level.room_threshold:
            break
        level.addRoom()
    level.add_doors()
    level.add_corridors()
    level.add_stairs()
    return level


def main(stdscr):
    map_width = 70
    map_height = 30
    room_threshold = random.randint(6, 10)
    depth = 10
    level = generate_level(map_width, map_height, room_threshold, depth)
    curses.curs_set(0)
    level.render(stdscr)
    stdscr.refresh()
    
    stdscr.getch()
    

if __name__ == "__main__":
    curses.wrapper(main)

