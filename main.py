import curses
import level
import random
import action

class Unit:
    def __init__(self, x, y, char='@'):
        self.x = x
        self.y = y
        self.char = char
        self.health = 100

class Game:
    def __init__(self, stdscr):
        curses.curs_set(0)  # Hide the cursor
        self.stdscr = stdscr
        map_width = 70
        map_height = 30
        room_threshold = random.randint(6, 10)
        self.depth = 0
        self.active_level = level.generate_level(map_width, map_height, room_threshold, self.depth)
        self.game_map = self.active_level.grid
        self.dungeon = dict({self.depth:self.active_level})

        self.player = Unit(self.active_level.up_stair[0], 
                           self.active_level.up_stair[1], '@')
        self.action_message = "What's the move, boss?"
        self.current_action = None

    def set_action_message(self, message):
        self.action_message = message

    def handle_input(self):
        key = self.stdscr.getch()
        if self.current_action:
            self.current_action.execute(key)
        elif key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            action.Move(self, key)
        elif key == ord('o'):
            action.Open(self, key)

    def render_map(self):
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                self.stdscr.addch(y, x, tile.char)

        self.stdscr.addch(self.player.y, self.player.x, self.player.char)
        
    def render_status_text(self):
        # Define the row from which to start displaying the text
        start_row = len(self.game_map)

        # Example status text, you can modify this based on the game state
        status_text = f"Health: {self.player.health} | Depth: {self.depth}"

        # Clear the previous status text
        self.stdscr.move(start_row, 0)
        self.stdscr.clrtoeol()

        # Display the new status text
        self.stdscr.addstr(start_row, 0, status_text)

    def render_action_message(self):
        # Define where to render the status message
        message_row = len(self.game_map) + 1 

        # Clear the previous message
        self.stdscr.move(message_row, 0)
        self.stdscr.clrtoeol()

        # Display the new message
        self.stdscr.addstr(message_row, 0, self.action_message)


    def run_game(self):
        while True:
            self.handle_input()
            self.stdscr.clear()
            self.render_map()
            self.render_status_text()
            self.render_action_message()
            self.stdscr.refresh()

def main(stdscr):
    game = Game(stdscr)
    game.run_game()

curses.wrapper(main)
