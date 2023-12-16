class MonsterData:
    '''
    This class stores data for various monster types in a structured format.
    Each monster is defined with the following attributes:

    - name: String representing the monster's name.
    - symbol: Identifier (usually a string) representing the monster's symbol.
    - level: Tuple containing level attributes:
        * lvl (int): The monster's difficulty level.
        * mov (int): The monster's movement rate.
        * ac (int): The monster's armor class.
        * mr (int): The monster's magic resistance.
        * aln (int): The monster's alignment.
    - gen_flags: Tuple containing generation flags, defining how the monster is generated in the game.
    - attacks: List of tuples, each representing an attack. Each tuple contains:
        * at (str): Type of attack.
        * ad (str): Type of damage dealt by the attack.
        * n (int): Number of dice used for the attack damage.
        * d (int): Number of sides on each die for the attack damage.
    - size: Tuple containing size attributes:
        * wt (int): Weight of the monster.
        * nut (int): Nutritional value of the monster.
        * snd (str): Sound made by the monster.
        * siz (str): Physical size of the monster.
    - mr1, mr2: Additional magic resistances or similar attributes.
    - flags1, flags2, flags3: Lists of strings representing various behavioral or characteristic flags.
    - color: String representing the monster's color.
    '''
    