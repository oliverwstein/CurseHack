class MonsterData:
    """
    The MonsterData class serves as a static repository for defining intrinsic attributes and characteristics of various monster types in the game. It's structured as a dictionary where each key is a monster type, and the value is a dictionary of attributes and flags specific to that monster type.

    Attributes:
        monsters (dict): A dictionary where each key is a unique monster identifier (e.g., "giant_ant", "python") and each value is a dictionary containing the intrinsic properties of that monster type. These properties include:

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
        MonsterData is used as a reference for creating instances of Monster class. It provides the base attributes which are then augmented or modified by the Monster class to represent individual monsters in the game.
    """
    monsters = {
        "giant_ant": {
            "name": "giant ant",
            "char": 'a',
            "level": 2,
            "exp": 18,
            "speed": 3, 
            "ac": 0,
            "mr": 0,
            "align": 0,
            "freq": 3,
            "weight": 10,
            "nutrition": 10,
            "size": "tiny",
            "color": "Brown",
            "attacks": (('AT_BITE', 'AD_PHYS', 1, 4)),
            "resists": (),
            "resists_conveyed": (),
            "geno": ("G_GENO", "G_SGROUP", "G_RANDOM"),
            "traits": ('TR_ANIMAL', 'TR_NOHANDS', 'TR_OVIPAROUS', 'TR_CARNIVORE')
            },
        "python": {
            "name": "python",
            "char": 'S',
            "level": 6,
            "exp": 82,
            "speed": 3, 
            "ac": 5,
            "mr": 0,
            "align": 0,
            "freq": 3,
            "weight": 250,
            "nutrition": 100,
            "size": "large",
            "color": "Magenta",
            "attacks": (('AT_BITE', 'AD_PHYS', 1, 4), ('AT_TUCH', 'AD_PHYS', 0, 0),
                        ('AT_HUGS', 'AD_WRAP', 1, 4), ('AT_HUGS', 'AD_PHYS', 2, 4)),
            "resists": (),
            "resists_conveyed": (),
            "geno": ("G_GENO", "G_RANDOM"),
            "traits": ('TR_SWIM', 'TR_NOLIMBS', 'TR_ANIMAL', 'TR_SLITHY', 'TR_CARNIVORE',
                        'TR_OVIPAROUS', 'TR_NOTAKE', 'TR_HOSTILE', 'TR_STRONG')
        },
    }

