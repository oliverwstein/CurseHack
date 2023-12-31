import random
from unit_data import UnitData

class Unit:
    def __init__(self, x, y, role, race, grade=1, char='@'):
        if role not in UnitData.classes:
            raise ValueError(f"Unknown unit class: {role}")
        if race not in UnitData.races:
            raise ValueError(f"Unknown unit race: {race}")

        self._x = x
        self._y = y
        self.symbol = char
        self.grade = grade
        self.role = role
        self.race = race

        # Initialize stats with base stats from class
        self.stats = UnitData.classes[role]['base_stats'].copy()
        self.growths = UnitData.classes[role]['growths'].copy()
        race_max_stats = UnitData.races[race]['max_stats']
        self.max_hp = UnitData.races[race]['hp']['starting'] + UnitData.classes[role]['hp']['starting']
        self.hp = self.max_hp
        self.ac = 10

        # Randomly increment stats until they sum to 75
        while sum(self.stats.values()) < 75:
            # Adjust growths for maxed out stats
            total_growth = sum(self.growths.values())
            if total_growth == 0:
                break  # Stop if all stats are maxed out

            # Choose a stat to increment based on growth probability
            rand_val = random.randint(1, total_growth)
            cumulative = 0
            for stat in self.stats:
                cumulative += self.growths[stat]
                if rand_val <= cumulative:
                    # Check if the stat is already at max for the race
                    if self.stats[stat] < race_max_stats[stat]:
                        self.stats[stat] += 1
                    else:
                        # Maxed out, set growth to zero
                        self.growths[stat] = 0
                    break

        self.speed = 12  # Default speed
        self.actions = self.calculate_actions()

    def calculate_actions(self):
        # Divide speed by 12 and separate the integer and fractional parts
        baseline_actions, fractional_chance = divmod(self.speed, 12)

        # Check if the fractional part warrants an extra action
        if random.random() < fractional_chance / 12:
            return baseline_actions + 1
        else:
            return baseline_actions

    def calculate_speed(self):
        # Modify speed based on factors like status effects
        return self.speed

    def alive(self):
        '''
        Check if the should be alive or dead.'''
        if self.hp <= 0:
            return False
        else:
            return True

    @property
    def pos(self):
        return (self._x, self._y)

    @pos.setter
    def pos(self, xy):
        if not isinstance(xy, tuple) or len(xy) != 2:
            raise ValueError("Position must be a tuple of two elements: (x, y)")
        self._x, self._y = xy
