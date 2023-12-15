import curses
import level
import random

class Unit:
    def __init__(self, x, y, char='@'):
        self.x = x
        self.y = y
        self.char = char

class Game:
    def __init__(self, stdscr):
        curses.curs_set(0)  # Hide the cursor
        self.stdscr = stdscr
        map_width = 70
        map_height = 30
        room_threshold = random.randint(6, 10)
        depth = 10
        self.active_level = level.generate_level(map_width, map_height, room_threshold, depth)
        self.game_map = self.active_level.grid

        self.player = Unit(self.active_level.up_stair[0], 
                           self.active_level.up_stair[1], '@')

    def handle_input(self):
        key = self.stdscr.getch()
        if key == curses.KEY_RIGHT:
            self.move(self.player, "right")
        elif key == curses.KEY_LEFT:
            self.move(self.player, "left")
        elif key == curses.KEY_DOWN:
            self.move(self.player, "down")
        elif key == curses.KEY_UP:
            self.move(self.player, "up")


    def move(self, unit, direction):
        new_x, new_y = unit.x, unit.y

        if direction == "right":
            new_x += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "up":
            new_y -= 1

        # Check if the move is legal before updating the unit's position
        if self.is_move_legal(new_x, new_y):
            unit.x, unit.y = new_x, new_y

    def is_move_legal(self, x, y):
        # Check the bounds of the map
        if x < 0 or y < 0 or x >= len(self.game_map[0]) or y >= len(self.game_map):
            return False

        # Check if the tile is walkable
        return self.game_map[y][x].walkable

    def render_map(self):
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                self.stdscr.addch(y, x, tile.char)

        self.stdscr.addch(self.player.y, self.player.x, self.player.char)  # Render player character

    def run_game(self):
        while True:
            self.handle_input()
            self.stdscr.clear()
            self.render_map()
            self.stdscr.refresh()

def main(stdscr):
    game = Game(stdscr)
    game.run_game()

curses.wrapper(main)
