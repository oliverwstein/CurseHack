import curses
import random
from heapq import heappop, heappush, heapify
import logging

class Rectangle:
    def __init__(self, x1, y1, width, height):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.area = self.width * self.height

    def __lt__(self, other):
        return self.area > other.area

    def choose_split_spot(self):
        rows = self.height
        cols = self.width
        if rows < 7 and cols < 7:
            return (-1, -1)
        elif rows < 7:
            axis = cols
            value = int(round(random.gauss((rows - 1) / 2, ((rows - 1) / 2)/ 2)))
            return (1, max(1, min(value, rows - 1)))
        elif cols < 7:
            axis = rows
        else:
            total_weight = rows + cols
            probability_1 = cols / total_weight
            if random.random() < probability_1:
                axis = cols
            else:
                axis = rows
        value = int(round(random.gauss((axis - 1) / 2, ((axis - 1) / 2)/ 2)))
        if axis is cols:
            return (1, max(1, min(value, axis - 1)))
        else:
            return (0, max(1, min(value, axis - 1)))


    def split_room(self, split = None, min_side_len = 5):

        if split is None:
            split = self.choose_split_spot()
        if split[0] == 0:
            # split on row split[1]
            rect_a = Rectangle(self.x1, self.y1, 
                            self.width, split[1] - random.randint(1, 2))
            rect_b = Rectangle(self.x1, self.y1 + split[1], 
                            self.width, self.height - (split[1]) - random.randint(1, 2))

        elif split[0] == 1:
            # split on col split[1]
            rect_a = Rectangle(self.x1, self.y1, 
                            split[1] - random.randint(1, 2), self.height)
            rect_b = Rectangle(self.x1 + split[1], self.y1, 
                            self.width - (split[1]) - random.randint(1, 2), self.height)
        else:
            # don't split the room.
            return None
        if (min(rect_a.width, rect_a.height) < min_side_len) and (min(rect_b.width, rect_b.height) < min_side_len):
            return None
        elif min(rect_a.width, rect_a.height) < min_side_len:
            return [rect_b]
        elif min(rect_b.width, rect_b.height) < min_side_len:
            return [rect_a]
        else:
            return [rect_a, rect_b]
    
class Level():

    def __init__(self, width, height, room_threshold, depth):
        self.width = width
        self.height = height
        self.area = width*height
        self.room_threshold = room_threshold
        self.depth = depth
        self.grid = grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        room = Rectangle(0, 0, self.height, self.width)
        self.room_heap = [room]
        heapify(self.room_heap)
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
        room_list = list(self.room_heap) + self.rooms_placed
        for room in room_list:
            for i in range(room.x1, room.x1 + room.width):
                for j in range(room.y1, room.y1 + room.height):
                    if 0 <= i < self.width and 0 <= j < self.height:
                        # Use '*' for interior parts of the room
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
        heap_info = f"Heap: {len(self.room_heap)}\n"
        for item in self.room_heap:
            heap_info += f"{item.x1}, {item.y1}, {item.width}, {item.height}\n"

        stdscr.addstr(0, 0, heap_info)
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

    def generateRooms(self):
        while len(self.room_heap) > 0:
            room = heappop(self.room_heap)
            if random.random() > 2*(1 - 0.5 * (room.area / (3 * self.area))):
                self.rooms_placed.append(room)
            else:
                new = room.split_room()
                if new == None:
                    self.rooms_placed.append(room)
                else:
                    for room in new:
                        heappush(self.room_heap, room)
        


def main(stdscr):
    map_width = 45
    map_height = 45
    room_threshold = 8
    level = Level(map_width, map_height, room_threshold, 10)
    level.generateRooms()
    level.grid = level.draw_grid()
    curses.curs_set(0)
    level.render(stdscr)
    stdscr.refresh()
    stdscr.getch()


def iterated_main(stdscr):
    map_width = 45
    map_height = 45
    room_threshold = 8
    level = Level(map_width, map_height, room_threshold, 10)

    while True:
        curses.curs_set(0)
        stdscr.clear()
        room_list = [x for x in level.room_heap]
        level.grid = level.draw_grid()
        room = heappop(level.room_heap)
        if random.random() > 1 - 0.5 * (room.area / (3 * level.area)):
            level.rooms_placed.append(room)
        else:
            new = room.split_room()
            if new == None:
                level.rooms_placed.append(room)
            else:
                for room in new:
                    heappush(level.room_heap, room)
        level.render(stdscr)
        stdscr.refresh()
        stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(iterated_main)
