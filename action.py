import curses
import level
class Action:
    def __init__(self, game, key):
        self.game = game
        self.execute(key)

    def execute(self, key):
        raise NotImplementedError("Execute method must be implemented by subclasses")

class Move(Action):
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
            self.move(self.game.player, direction)
    
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

        elif isinstance(self.game.game_map[new_y][new_x], level.Door):
            self.game.set_action_message("The door is closed. Press 'o' to try opening it.")

    def is_move_legal(self, x, y):
        # Check the bounds of the map
        if x < 0 or y < 0 or x >= len(self.game.game_map[0]) or y >= len(self.game.game_map):
            return False

        # Check if the tile is walkable
        return self.game.game_map[y][x].walkable
    
class Climb(Action):
    def execute(self, key):
        direction = ""
        if key == ord('<'):
            direction = "up"
        elif key == ord('>'):
            direction = "down"

        if direction:
            self.try_climb(direction)
    
    def try_climb(self, direction):
        x, y = self.game.player.pos()
        if self.game.game_map[y][x].tile_type == direction:
            if direction == "down":
                self.game.depth += 1
                self.game.dungeon[self.game.depth] = level.generate_level(self.game.map_width, self.game.map_height, self.game.room_threshold, self.game.depth)
                self.game.active_level = self.game.dungeon[self.game.depth]
                self.game.game_map = self.game.active_level.grid
                self.game.player.x = self.game.active_level.up_stair.x
                self.game.player.y = self.game.active_level.up_stair.y
                self.game.set_action_message("Onward and downward!")
            if direction == "up":
                if self.game.depth > 0:
                    self.game.depth -= 1
                    self.game.dungeon[self.game.depth]
                    self.game.active_level = self.game.dungeon[self.game.depth]
                    self.game.game_map = self.game.active_level.grid
                    self.game.player.x = self.game.active_level.down_stair.x
                    self.game.player.y = self.game.active_level.down_stair.y
                    self.game.set_action_message("Was that was too deep for you?")
            
            

class Open(Action):
    def execute(self, key):
        if key == ord('o'):
            self.game.set_action_message("In what direction?")
            self.game.current_action = self
        else:
            # Handle the directional input for the 'open' action
            self.handle_directional_open(key)
            self.game.current_action = None

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
        player_x, player_y = self.game.player.x, self.game.player.y
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
        if isinstance(self.game.game_map[target_y][target_x], level.Door):
            if self.game.game_map[target_y][target_x].state == 'closed':
                self.game.game_map[target_y][target_x].open()
                self.game.set_action_message("You open the door.")
            else:
                self.game.game_map[target_y][target_x].close()
                self.game.set_action_message("You close the door.")
        else:
            self.game.set_action_message("There's nothing to open in that direction.")
