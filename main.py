import curses

class Unit:
    def __init__(self, x, y, char='@'):
        self.x = x
        self.y = y
        self.char = char

class Game:
    def __init__(self, stdscr):
        curses.curs_set(0)  # Hide the cursor
        self.stdscr = stdscr
        self.player = Unit(0, 0, '@')
        self.game_map = [['.' for _ in range(20)] for _ in range(10)]

    def handle_input(self):
        key = self.stdscr.getch()
        if key == curses.KEY_RIGHT:
            self.player.x += 1
        elif key == curses.KEY_LEFT:
            self.player.x -= 1
        elif key == curses.KEY_DOWN:
            self.player.y += 1
        elif key == curses.KEY_UP:
            self.player.y -= 1

    def render_map(self):
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                self.stdscr.addch(y, x, tile)

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
