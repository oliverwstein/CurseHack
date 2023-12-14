import curses
import random

class Rectangle:
    def __init__(self, x1, y1, width, height):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.area = self.width * self.height

    
class Level():

    def __init__(self, width, height, room_threshold, depth):
        self.width = width
        self.height = height
        self.area = width*height
        self.room_threshold = room_threshold
        self.depth = depth
        self.grid = grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.rooms_placed = []


    def add_room_to_grid(self, room, char = '#'):
        for i in range(room.x1, room.x1 + room.width):
                for j in range(room.y1, room.y1 + room.height):
                    if 0 <= i < self.width and 0 <= j < self.height:
                        self.grid[j][i] = char

    def draw_grid(self):
        # Define Unicode corner characters
        bottom_left_corner = '\u2514'
        top_right_corner = '\u2510'
        top_left_corner = '\u250C'
        bottom_right_corner = '\u2518'
        grid = [['\u2591' for _ in range(self.width)] for _ in range(self.height)]
        room_list = self.rooms_placed
        for room in room_list:
            for i in range(room.x1, room.x1 + room.width):
                for j in range(room.y1, room.y1 + room.height):
                    if 0 <= i < self.width and 0 <= j < self.height:
                        # Use "*" for interior parts of the room
                        grid[j][i] = "*"

                        # Check if it's an edge and update the character accordingly
                        if i == room.x1 or i == room.x1 + room.width - 1:
                            grid[j][i] = "|"
                        if j == room.y1 or j == room.y1 + room.height - 1:
                            grid[j][i] = "-"

                        # Check if it's a corner and update the character accordingly
                        if (i, j) == (room.x1, room.y1):
                            grid[j][i] = top_left_corner
                        elif (i, j) == (room.x1 + room.width - 1, room.y1):
                            grid[j][i] = top_right_corner
                        elif (i, j) == (room.x1, room.y1 + room.height - 1):
                            grid[j][i] = bottom_left_corner
                        elif (i, j) == (room.x1 + room.width - 1, room.y1 + room.height - 1):
                            grid[j][i] = bottom_right_corner

        return grid

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
            room = Rectangle(x1, y1, width, height)
            if self.is_valid_placement(room):
                self.rooms_placed.append(room)
                return True
        return False
        
    def is_valid_placement(self, new_room, buffer = 3):
        for rect in self.rooms_placed:
            if (new_room.x1 < rect.x1 + rect.width + buffer and
                    new_room.x1 + new_room.width + buffer > rect.x1 and
                    new_room.y1 < rect.y1 + rect.height + buffer and
                    new_room.y1 + new_room.height + buffer > rect.y1):
                # Rectangles are too close
                return False
        # No overlap with any existing rectangle
        return True
    
    def sort_rooms(self):
        self.rooms_placed = sorted(self.rooms_placed, key=lambda room: (room.x1, room.y1))

    def make_corridors(self):
        n_rooms = len(self.rooms_placed)

        # First Step: Join each room to the next one in the sequence
        for a in range(n_rooms - 1):
            self.join_rooms(a, a + 1, 100)
            if random.random() < 0.02:
                break

        # Second Step: Join each room to the room two steps down the array
        for a in range(n_rooms - 2):
            self.join_rooms(a, a + 2, 15)

        # Third Step: Join each room to every other room
        for a in range(n_rooms):
            for b in range(n_rooms):
                if a != b:
                    self.join_rooms(a, b, 10)

        # Fourth Step: Join random pairs of rooms
        if n_rooms > 2:
            for i in range(random.randint(4, n_rooms + 4)):
                a = random.randint(0, n_rooms - 1)
                b = random.randint(0, n_rooms - 3)
                if b >= a:
                    b += 2
                self.join_rooms(a, b, 10)

    def join_rooms(self, a, b, max_corridor_length):
        # Your logic for joining rooms goes here
        room_a = self.rooms_placed[a]
        room_b = self.rooms_placed[b]

        # Identify connection points and generate corridor path
        start = (room_a.x1 + room_a.width // 2, room_a.y1 + room_a.height // 2)
        end = (room_b.x1 + room_b.width // 2, room_b.y1 + room_b.height // 2)
        corridor_path = self.generate_corridor(start, end, max_corridor_length)

        # Update grid with corridor path
        for x, y in corridor_path:
            if 0 <= x < self.width and 0 <= y < self.height:
                if self.grid[y][x] == '\u2591':
                    self.grid[y][x] = "#"
    
    def generate_corridor(self, start, end, max_corridor_length):
        corridor_path = []
        x, y = start
        dx = end[0] - x
        dy = end[1] - y

        # Bresenham's line algorithm
        x_step = 1 if dx > 0 else -1
        y_step = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            p = 2 * dy - dx
            while x != end[0]:
                corridor_path.append((x, y))
                x += x_step
                if p >= 0:
                    y += y_step
                    p -= 2 * dx
                    # Update the flanking tile to prevent diagonal movement
                    corridor_path.append((x, y - y_step))
                    corridor_path.append((x - x_step, y))
                p += 2 * dy
        else:
            p = 2 * dx - dy
            while y != end[1]:
                corridor_path.append((x, y))
                y += y_step
                if p >= 0:
                    x += x_step
                    p -= 2 * dy
                    # Update the flanking tile to prevent diagonal movement
                    corridor_path.append((x - x_step, y))
                    corridor_path.append((x, y - y_step))
                p += 2 * dx

        # Check if the corridor path length exceeds the maximum length
        if len(corridor_path) > max_corridor_length:
            return []  # Return an empty list if the corridor is too long
        else:
            return corridor_path  # Return the generated corridor path

def main(stdscr):
    map_width = 70
    map_height = 30
    room_threshold = random.randint(6, 10)
    level = Level(map_width, map_height, room_threshold, 10)
    space = True
    while space:
        if len(level.rooms_placed) >= level.room_threshold:
            break
        level.addRoom()
    level.grid = level.draw_grid()
    curses.curs_set(0)
    level.make_corridors()
    level.render(stdscr)
    stdscr.refresh()
    
    stdscr.getch()
    

if __name__ == "__main__":
    curses.wrapper(main)

