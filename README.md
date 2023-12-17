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
- **Purpose**: Defines various actions a player can perform in the game.
- **Functionality**: Action base class, move action, climb action, and open action.

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
- **Purpose**: [Description of the monster file – still in progress].

## Installation and Running
- **Requirements**: Python 3.x, curses library.
- **Running the Game**: Execute `main.py` using Python.

## Future Enhancements
- Continued development of `monster.py`.
- Additional features and improvements as per game development progress.

## Contribution Guidelines
- [Your guidelines for contributors, if any].
