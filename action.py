import curses
import level
class Action:
    """
    The `Action` class serves as a base class for defining various actions that a player can take in the game.
    Subclasses of Action implement specific actions like moving, opening doors, or climbing stairs.

    Attributes:
        game (Game): The instance of the game where the action is being executed.
    
    Functions:
        __init__(game, key): Initializes the action with the game instance and the key pressed.
        execute(key): Abstract method to be implemented by subclasses to define specific action behavior.
    """
    def __init__(self, game, key):
        self.game = game
        self.execute(key)

    def execute(self, key):
        raise NotImplementedError("Execute method must be implemented by subclasses")

class Move(Action):
    """
    The `Move` class handles the movement of the player's character in the game.

    Functions:
        execute(key): Executes the move action based on the key pressed.
        move(unit, direction): Moves the specified unit in the given direction if the move is legal.
        is_move_legal(x, y): Checks if a move to the specified coordinates is legal.
    """
    def __init__(self, game, key, obj):
        self.unit = obj
        super().__init__(game, key)
        

    def execute(self, key):
        direction = ""
        if key == curses.KEY_RIGHT:
            direction = "right"
        elif key == curses.KEY_LEFT:
            direction = "left"
        elif key == curses.KEY_DOWN:
            direction = "down"
        elif key == curses.KEY_UP:
            direction = "up"

        if direction:
            self.move(direction)
            self.unit.actions -= 1
    
    def move(self, direction):
        new_x, new_y = self.unit.pos

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
            self.unit.pos = new_x, new_y

        elif isinstance(self.game.game_map[new_x][new_y], level.Door):
            self.game.set_action_message("The door is closed. Press 'o' to try opening it.")

    def is_move_legal(self, x, y):
        # Check the bounds of the map
        if x < 0 or y < 0 or x >= len(self.game.game_map) or y >= len(self.game.game_map[0]):
            return False

        # Check if the tile is walkable
        return self.game.game_map[x][y].walkable
    
class Climb(Action):
    """
    The `Climb` class allows the player's character to climb up or down stairs in the game.

    Functions:
        execute(key): Executes the climb action based on the key pressed.
        try_climb(direction): Attempts to climb in the specified direction.
    """
    def execute(self, key):
        direction = ""
        if key == ord('<'):
            direction = "up"
        elif key == ord('>'):
            direction = "down"

        if direction:
            self.try_climb(direction)
        self.game.player.actions -= 1
    
    def try_climb(self, direction):
        x, y = self.game.player.pos
        if self.game.game_map[x][y].tile_type == direction:
            if direction == "down":
                self.game.depth += 1
                self.game.dungeon[self.game.depth] = level.generate_level(self.game.map_width, self.game.map_height, self.game.room_threshold, self.game.depth)
                self.game.active_level = self.game.dungeon[self.game.depth]
                self.game.game_map = self.game.active_level.grid
                self.game.player.pos = self.game.active_level.up_stair.pos
                self.game.set_action_message("Onward and downward!")
            if direction == "up":
                if self.game.depth > 0:
                    self.game.depth -= 1
                    self.game.dungeon[self.game.depth]
                    self.game.active_level = self.game.dungeon[self.game.depth]
                    self.game.game_map = self.game.active_level.grid
                    self.game.player.pos = self.game.active_level.down_stair.pos
                    self.game.set_action_message("Was that was too deep for you?")
            
            

class Open(Action):
    """
    The `Open` class manages the action of opening or closing doors within the game.

    Functions:
        execute(key): Executes the open action based on the key pressed.
        handle_directional_open(key): Handles the direction-specific logic for opening a door.
        try_open(direction): Attempts to open or close a door in the specified direction.
    """
    def execute(self, key):
        if key == ord('o'):
            self.game.set_action_message("In what direction?")
            self.game.current_action = self
        else:
            # Handle the directional input for the 'open' action
            self.handle_directional_open(key)
            self.game.current_action = None
        self.game.player.actions -= 1

    def handle_directional_open(self, key):
        direction = ""
        if key == curses.KEY_RIGHT:
            direction = "right"
        elif key == curses.KEY_LEFT:
            direction = "left"
        elif key == curses.KEY_DOWN:
            direction = "down"
        elif key == curses.KEY_UP:
            direction = "up"

        if direction:
            self.try_open(direction)
            self.game.awaiting_direction = False
        else:
            self.game.set_action_message("Invalid direction. Please use arrow keys.")

    def try_open(self, direction):
        player_x, player_y = self.game.player.pos
        target_x, target_y = player_x, player_y

        if direction == "right":
            target_x += 1
        elif direction == "left":
            target_x -= 1
        elif direction == "down":
            target_y += 1
        elif direction == "up":
            target_y -= 1
        # Check if there's a door in the target direction
        if isinstance(self.game.game_map[target_x][target_y], level.Door):
            if self.game.game_map[target_x][target_y].state == 'closed':
                self.game.game_map[target_x][target_y].open()
                self.game.set_action_message("You open the door.")
            else:
                self.game.game_map[target_x][target_y].close()
                self.game.set_action_message("You close the door.")
        else:
            self.game.set_action_message("There's nothing to open in that direction.")
