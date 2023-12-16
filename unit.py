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
        self.char = char
        self.grade = grade
        self.role = role
        self.race = race

        # Initialize stats with base stats from class
        self.stats = UnitData.classes[role]['base_stats'].copy()
        self.growths = UnitData.classes[role]['growths'].copy()
        race_max_stats = UnitData.races[race]['max_stats']

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

    @property
    def pos(self):
        return (self._x, self._y)

    @pos.setter
    def pos(self, xy):
        if not isinstance(xy, tuple) or len(xy) != 2:
            raise ValueError("Position must be a tuple of two elements: (x, y)")
        self._x, self._y = xy
