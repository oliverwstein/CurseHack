# CurseHack: A Python Curses-Based Roguelike Game

## Overview
CurseHack is a roguelike game inspired by NetHack, developed in Python using the Curses library. It features dynamic level generation, a variety of actions for player interaction, and a rich set of units and monsters, each with distinct attributes.

## Key Components

### `main.py`
- **Purpose**: Entry point for the game, initializing the game environment and handling the main game loop.
- **Key Features**: Initializes game settings, manages game actions and user inputs, and renders the game map, player status, and action messages.

### `level.py`
- **Purpose**: Manages the creation, layout, and rendering of game levels.
- **Functionality**: Includes level generation, room placement, map-related utilities, rendering, and corridor generation using Kruskal's algorithm.

### `room.py`
- **Purpose**: Handles creation and attributes of individual rooms within a game level.
- **Functionality**: Room initialization, door generation, feature handling, and utility functions for feature positioning.

### `action.py`
- **Purpose**: Defines various actions the player (and monsters) can perform in the game.
- **Functionality**: Action base class, move action, climb action, open action, attack action.

### `tile.py`
- **Purpose**: Defines the `Tile` class and its subclasses for different game map elements.
- **Functionality**: Includes a variety of tiles like corridors, doors, walls, stairs, floors, and environmental features.

### `feature.py`
- **Purpose**: Manages creation and attributes of various features in the game.
- **Functionality**: Feature initialization, tile generation, random feature selection, and utility methods.

### `feature_data.py`
- **Purpose**: Serves as a data repository for defining properties and characteristics of various features.
- **Content**: Contains a dictionary mapping feature names to properties like tile type, state, color, and rarity.

### `unit.py`
- **Purpose**: Manages player character's (Unit) attributes and states.
- **Functionality**: Initialization, stats management, stat incrementation, and position handling.

### `unit_data.py`
- **Purpose**: Provides data structures for defining classes and races of units.
- **Content**: Specifies base stats and growth rates for unit classes and maximum stats for races.

### `monster.py`
- **Purpose**: Manages the attributes and behaviors of monsters in the game.
- **Functionality**:
  - **Monster Class**: Represents a monster (NPC) in the game. Each monster instance is created with a set of attributes defined in `MonsterData`.
  - **Key Attributes**:
    - Basic Attributes: Includes name, symbol, level, experience, speed, armor class, magic resistance, alignment, frequency, weight, nutritional value, size, color.
    - Combat Attributes: Defines the monster's attack types, resistances, resistances conveyed, and genetic flags.
    - Behavioral Attributes: Specifies traits or behaviors of the monster.
  - **Dynamic Calculations**:
    - `calculate_actions()`: Determines the number of actions a monster can perform in a turn, based on its speed.
    - `calculate_hp()`: Calculates the monster's hit points based on its level.
    - `alive()`: Checks the monster's living status.
  - **Position Handling**:
    - The position of the monster (`pos`) is managed with getter and setter methods.
  - **Random Monster Generation**:
    - `random_monster_based_on_rarity()`: Selects a monster based on its rarity and specified attributes.
  - **Usage**: Used to create and manage individual monster instances in the game, each with unique characteristics and abilities.
- **Dependencies**: Requires `monster_data.py` for monster attributes and `random` module for probabilistic calculations.


## Installation and Running
- **Requirements**: Python 3.x, curses library.
- **Running the Game**: Execute `main.py` using Python.

## Future Enhancements
- Continued development of `monster.py`.
- Additional features and improvements as per game development progress.

## Contribution Guidelines
- [Your guidelines for contributors, if any].
