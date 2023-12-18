import curses
import level
import random
import action
from unit import *

class Game:
    """
    The `Game` class serves as the core controller of the game. It manages the game loop,
    user input, rendering of the game state, and the interactions between various game components.

    Attributes:
        stdscr: A Curses window object, representing the standard screen for the game's output.
        map_width, map_height: Dimensions of the game map.
        room_threshold: A randomly determined threshold for room generation within a level.
        depth: Represents the current depth level of the dungeon.
        active_level: An instance of `Level`, representing the current level of the dungeon.
        game_map: The grid representation of the current level.
        dungeon: A dictionary holding different levels of the dungeon.
        player: An instance of `Unit`, representing the player's character.
        action_message: A message string displayed to the player based on actions.
        current_action: Stores the current action being executed by the player.

    Functions:
        __init__(stdscr): Initializes the game environment, sets up the first level,
                          and prepares the player character.
        set_action_message(message): Updates the action message displayed to the player.
        handle_input(): Manages user input, directing to appropriate action classes or handling navigation.
        render_map(): Renders the current state of the game map to the standard screen.
        render_status_text(): Displays the status text, including player race, role, level, and dungeon depth.
        render_action_message(): Shows the current action message to the player.
        run_game(): Contains the main game loop, continuously handling input, rendering the game state,
                    and refreshing the screen.

    Interaction with Other Classes:
        Level (`level.py`): Utilized to generate and manage the current level of the dungeon.
        Unit (`unit.py`): Represents the player character, with its state and actions within the game.
        Action (`action.py`): Actions like `Move`, `Open`, `Climb` are instantiated based on user input
                              to affect the game state.
    
    Usage:
        The `Game` class is instantiated and run within the `main(stdscr)` function.
        It is the central orchestrator of the game, tying together user interactions,
        game state management, and rendering.
    """
    def __init__(self, stdscr):
        curses.curs_set(0)  # Hide the cursor
        self.stdscr = stdscr
        self.map_width = 70
        self.map_height = 30
        self.room_threshold = random.randint(6, 10)
        self.depth = 0
        self.active_level = level.generate_level(self.map_width, self.map_height, self.room_threshold, self.depth)
        self.game_map = self.active_level.grid
        self.dungeon = dict({self.depth:self.active_level})

        self.player = Unit(*self.active_level.up_stair.pos, role = 'Wizard', race = 'Human', char  = '@')
        self.action_message = "What's the move, boss?"
        self.current_action = None
        self.turn = 1

    def set_action_message(self, message):
        self.action_message = message

    def handle_input(self):
        key = self.stdscr.getch()
        self.action_message = "What's the move, boss?"
        if self.current_action:
            self.current_action.execute(key)
        elif key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            action.Move(self, key)
        elif key == ord('o'):
            action.Open(self, key)
        elif key in [ord('<'), ord('>')]:
            action.Climb(self, key)

    def render_map(self):
        for x, column in enumerate(self.game_map):
            for y, tile in enumerate(column):
                # Ensure x, y are within the bounds of the stdscr dimensions
                if 0 <= y < curses.LINES and 0 <= x < curses.COLS:
                    try:
                        self.stdscr.addch(y, x, tile.char)
                    except curses.error:
                        pass  # Ignore curses error if a character cannot be added

        # Ensure the player's position is within the bounds before drawing
        player_x, player_y = self.player.pos
        if 0 <= player_y < curses.LINES and 0 <= player_x < curses.COLS:
            try:
                self.stdscr.addch(player_y, player_x, self.player.char)
            except curses.error:
                pass  # Ignore curses error if a character cannot be added
        
        # Render each monster
        for monster in self.active_level.monsters:
            monster_x, monster_y = monster.pos
            if 0 <= monster_y < curses.LINES and 0 <= monster_x < curses.COLS:
                try:
                    self.stdscr.addch(monster_y, monster_x, monster.char)
                except curses.error:
                    pass  # Ignore curses error if a character cannot be added
        
    def render_status_text(self):
        # Define the row from which to start displaying the text
        start_row = len(self.game_map[0])

        # Example status text, you can modify this based on the game state
        status_text = f"{self.player.race} {self.player.role} | Player Level: {self.player.grade} | Depth: {self.depth} | Turn: {self.turn}"

        # Clear the previous status text
        self.stdscr.move(start_row, 0)
        self.stdscr.clrtoeol()

        # Display the new status text
        self.stdscr.addstr(start_row, 0, status_text)

    def render_action_message(self):
        # Define where to render the status message
        message_row = len(self.game_map[0]) + 1 

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
            if self.player.actions == 0:
                self.npc_actions()
                self.end_turn()

    def end_turn(self):
        self.player.actions = self.player.calculate_actions()
        for monster in self.active_level.monsters:
            monster.actions = monster.calculate_actions()
        self.turn += 1
    
    def npc_actions(self):
        while any(monster.actions > 0 for monster in self.active_level.monsters):
            for monster in self.active_level.monsters:
                if monster.actions > 0:
                    monster.take_action()
                    monster.actions -= 1

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    game = Game(stdscr)
    game.run_game()

curses.wrapper(main)
