from monster_data import MonsterData
import random

class Attack:
    """
    Represents a specific type of attack that a monster can perform.

    Attributes:
        attack_type (str): The type of attack (e.g., bite, claw).
        damage_type (str): The type of damage inflicted by the attack (e.g., physical, fire).
        num_dice (int): The number of dice to roll for determining damage.
        num_sides (int): The number of sides on each die used for the damage roll.
    """
    def __init__(self, attack_type, damage_type, num_dice, num_sides):
        self.attack_type = attack_type  # Type of attack (e.g., bite, claw)
        self.damage_type = damage_type  # Type of damage (e.g., physical, fire)
        self.num_dice = num_dice        # Number of dice to roll for damage
        self.num_sides = num_sides      # Number of sides on each die

class Monster:
    """
    Represents a monster (NPC) in the game, with attributes defined in MonsterData.

    The Monster class is instantiated with a specific type of monster. It fetches the corresponding 
    data from the MonsterData class and sets its own attributes based on this data.

    Attributes:
        - name (str): The display name of the monster.
        - char (str): A symbol representing the monster type.
        - level (int): The base level of the monster.
        - exp (int): The base experience provided by the monster.
        - speed (int): The base speed of the monster.
        - ac (int): The base armor class of the monster.
        - mr (int): The base magic resistance of the monster.
        - align (int): The alignment of the monster.
        - freq (int): The frequency of the monster's occurrence.
        - weight (int): The weight of the monster.
        - nutrition (int): The nutritional value of the monster.
        - size (str): The size category of the monster.
        - color (str): The color of the monster.
        - attacks (tuple): A tuple of attack types and their effects.
        - resists (tuple): A tuple of resistances that the monster has.
        - resists_conveyed (tuple): A tuple of resistances that the monster can convey.
        - geno (tuple): Genetic flags related to monster generation.
        - traits (tuple): A tuple of traits or behaviors of the monster.

    Usage:
        Monster instances are created to represent individual monsters in the game, 
        each with their own set of attributes and abilities as defined in MonsterData.
    """
    def __init__(self, x, y, name = None):
        self._x = x
        self._y = y
        if name is None:
            name = self.random_monster_based_on_rarity()

        if name not in MonsterData.monsters:
            raise ValueError(f"Unknown monster name: {name}")

        monster_data = MonsterData.monsters[name]

        self.name = name
        self.char = monster_data["char"]
        self.level = monster_data["level"]
        self.exp = monster_data["level"]
        self.speed = monster_data["speed"]
        self.armor_class = monster_data["ac"]
        self.magic_resistance  = monster_data["mr"]
        self.align  = monster_data["align"]
        self.freq  = monster_data["freq"]
        self.size = monster_data["size"]
        self.weight = monster_data["weight"]
        self.nutrition = monster_data["nutrition"]
        self.attacks = monster_data["attacks"]
        self.resists = monster_data["resists"]
        self.resists_conveyed = monster_data["resists_conveyed"]
        self.geno = monster_data["geno"]
        self.traits = monster_data["traits"]
        self.color = monster_data["color"]
        self.actions = self.calculate_actions()
    @staticmethod
    def random_monster_based_on_rarity(monster_names=None):
        if monster_names is None:
            # Filter only the specified monsters that are eligible for random generation
            filtered_monsters = {name: attrs for name, attrs in MonsterData.monsters.items() if "G_RANDOM" in attrs.get("geno", [])}
        else:
            lured_monsters = {key: MonsterData.monsters[key] for key in monster_names if key in  MonsterData.monsters}
            # Filter only the specified monsters that are eligible for random generation
            filtered_monsters = {name: attrs for name, attrs in lured_monsters.items() if "G_RANDOM" in attrs.get("geno", [])}
            if len(filtered_monsters) == 0 :
                filtered_monsters = {name: attrs for name, attrs in MonsterData.monsters.items() if "G_RANDOM" in attrs.get("geno", [])}

        
        # Group monsters by rarity
        rarity_groups = {}
        for name, attrs in filtered_monsters.items():
            rarity = attrs['freq']  # Assuming 'freq' indicates rarity
            rarity_groups.setdefault(rarity, []).append(name)
        # Calculate weights for each rarity group and normalize within the group
    
        normalized_weights = {}
        for rarity, monsters in rarity_groups.items():
            group_weight = 1 / (2 ** rarity)
            weight_per_monster = group_weight / len(monsters)
            for monster in monsters:
                normalized_weights[monster] = weight_per_monster

        options, weights = zip(*normalized_weights.items())
    
        return random.choices(options, weights, k=1)[0]

    

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

    def take_action(self):
        pass

    @property
    def pos(self):
        return (self._x, self._y)

    @pos.setter
    def pos(self, xy):
        if not isinstance(xy, tuple) or len(xy) != 2:
            raise ValueError("Position must be a tuple of two elements: (x, y)")
        self._x, self._y = xy



