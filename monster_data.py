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
    monsters = {
        {
        {
            'giant_ant': {
                'name': 'giant ant',
                'symbol': 'S_ANT',
                'level': [
                    '2',
                    '18',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'killer_bee': {
                'name': 'killer bee',
                'symbol': 'S_ANT',
                'level': [
                    '1',
                    '18',
                    '-1',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_LGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_STNG',
                        'AD_DRST',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '1',
                    '5',
                    'MS_BUZZ',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_FLY',
                    'M1_NOHANDS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_FEMALE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_YELLOW'
            },
            'soldier_ant': {
                'name': 'soldier ant',
                'symbol': 'S_ANT',
                'level': [
                    '3',
                    '18',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_STNG',
                        'AD_DRST',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    '20',
                    '5',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_POIS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLUE'
            },
            'fire_ant': {
                'name': 'fire ant',
                'symbol': 'S_ANT',
                'level': [
                    '3',
                    '18',
                    '3',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_FIRE',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '30',
                    '10',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'giant_beetle': {
                'name': 'giant beetle',
                'symbol': 'S_ANT',
                'level': [
                    '5',
                    '6',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_POIS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLACK'
            },
            'queen_bee': {
                'name': 'queen bee',
                'symbol': 'S_ANT',
                'level': [
                    '9',
                    '24',
                    '-4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_STNG',
                        'AD_DRST',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '1',
                    '5',
                    'MS_BUZZ',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_FLY',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_FEMALE',
                    'M2_PRINCE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_LORD'
            },
            'acid_blob': {
                'name': 'acid blob',
                'symbol': 'S_BLOB',
                'level': [
                    '1',
                    '3',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_ACID',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '30',
                    '10',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_ACID'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'quivering_blob': {
                'name': 'quivering blob',
                'symbol': 'S_BLOB',
                'level': [
                    '5',
                    '1',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '200',
                    '100',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_WHITE'
            },
            'gelatinous_cube': {
                'name': 'gelatinous cube',
                'symbol': 'S_BLOB',
                'level': [
                    '6',
                    '6',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_PLYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_NONE',
                        'AD_PLYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '600',
                    '150',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_OMNIVORE',
                    'M1_ACID'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_CYAN'
            },
            'chickatrice': {
                'name': 'chickatrice',
                'symbol': 'S_COCKATRICE',
                'level': [
                    '4',
                    '4',
                    '8',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '2'
                    ),
                    (
                        'AT_TUCH',
                        'AD_STON',
                        '0',
                        '0'
                    ),
                    (
                        'AT_NONE',
                        'AD_STON',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_HISS',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'cockatrice': {
                'name': 'cockatrice',
                'symbol': 'S_COCKATRICE',
                'level': [
                    '5',
                    '6',
                    '6',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '5'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_TUCH',
                        'AD_STON',
                        '0',
                        '0'
                    ),
                    (
                        'AT_NONE',
                        'AD_STON',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '30',
                    '30',
                    'MS_HISS',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OMNIVORE',
                    'M1_OVIPAROUS'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_YELLOW'
            },
            'pyrolisk': {
                'name': 'pyrolisk',
                'symbol': 'S_COCKATRICE',
                'level': [
                    '6',
                    '6',
                    '6',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_GAZE',
                        'AD_FIRE',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '30',
                    '30',
                    'MS_HISS',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_POISON',
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OMNIVORE',
                    'M1_OVIPAROUS'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'jackal': {
                'name': 'jackal',
                'symbol': 'S_DOG',
                'level': [
                    '0',
                    '12',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '2'
                    )
                ],
                'size': (
                    '300',
                    '250',
                    'MS_BARK',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'fox': {
                'name': 'fox',
                'symbol': 'S_DOG',
                'level': [
                    '0',
                    '15',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '300',
                    '250',
                    'MS_BARK',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'coyote': {
                'name': 'coyote',
                'symbol': 'S_DOG',
                'level': [
                    '1',
                    '12',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '300',
                    '250',
                    'MS_BARK',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'werejackal': {
                'name': 'werejackal',
                'symbol': 'S_HUMAN',
                'level': [
                    '2',
                    '12',
                    '10',
                    '10',
                    '-7'
                ],
                'gen_flags': (
                    '1',
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_WERE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_WERE',
                    'M2_HOSTILE',
                    'M2_HUMAN',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'little_dog': {
                'name': 'little dog',
                'symbol': 'S_DOG',
                'level': [
                    '2',
                    '18',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '150',
                    '150',
                    'MS_BARK',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'dingo': {
                'name': 'dingo',
                'symbol': 'S_DOG',
                'level': [
                    '4',
                    '16',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '400',
                    '200',
                    'MS_BARK',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_YELLOW'
            },
            'dog': {
                'name': 'dog',
                'symbol': 'S_DOG',
                'level': [
                    '4',
                    '16',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '400',
                    '200',
                    'MS_BARK',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'large_dog': {
                'name': 'large dog',
                'symbol': 'S_DOG',
                'level': [
                    '6',
                    '15',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '800',
                    '250',
                    'MS_BARK',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'wolf': {
                'name': 'wolf',
                'symbol': 'S_DOG',
                'level': [
                    '5',
                    '12',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '500',
                    '250',
                    'MS_BARK',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'werewolf': {
                'name': 'werewolf',
                'symbol': 'S_HUMAN',
                'level': [
                    '5',
                    '12',
                    '10',
                    '20',
                    '-7'
                ],
                'gen_flags': (
                    '1',
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_WERE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_WERE',
                    'M2_HOSTILE',
                    'M2_HUMAN',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_ORANGE'
            },
            'winter_wolf_cub': {
                'name': 'winter wolf cub',
                'symbol': 'S_DOG',
                'level': [
                    '5',
                    '12',
                    '4',
                    '0',
                    '-5'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_BREA',
                        'AD_COLD',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '250',
                    '200',
                    'MS_BARK',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_CYAN'
            },
            'warg': {
                'name': 'warg',
                'symbol': 'S_DOG',
                'level': [
                    '7',
                    '12',
                    '4',
                    '0',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '850',
                    '350',
                    'MS_BARK',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'winter_wolf': {
                'name': 'winter wolf',
                'symbol': 'S_DOG',
                'level': [
                    '7',
                    '12',
                    '4',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_BREA',
                        'AD_COLD',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '700',
                    '300',
                    'MS_BARK',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_CYAN'
            },
            'hell_hound_pup': {
                'name': 'hell hound pup',
                'symbol': 'S_DOG',
                'level': [
                    '7',
                    '12',
                    '4',
                    '20',
                    '-5'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_BREA',
                        'AD_FIRE',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '200',
                    '200',
                    'MS_BARK',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'hell_hound': {
                'name': 'hell hound',
                'symbol': 'S_DOG',
                'level': [
                    '12',
                    '14',
                    '2',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_BREA',
                        'AD_FIRE',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '600',
                    '300',
                    'MS_BARK',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'cerberus': {
                'name': 'Cerberus',
                'symbol': 'S_DOG',
                'level': [
                    '12',
                    '10',
                    '2',
                    '20',
                    '-7'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ',
                    'G_HELL'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '1000',
                    '350',
                    'MS_BARK',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_PNAME',
                    'M2_MALE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'gas_spore': {
                'name': 'gas spore',
                'symbol': 'S_EYE',
                'level': [
                    '1',
                    '3',
                    '10',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BOOM',
                        'AD_PHYS',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'floating_eye': {
                'name': 'floating eye',
                'symbol': 'S_EYE',
                'level': [
                    '2',
                    '1',
                    '9',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '5'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_PLYS',
                        '0',
                        '70'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_AMPHIBIOUS',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLUE'
            },
            'freezing_sphere': {
                'name': 'freezing sphere',
                'symbol': 'S_EYE',
                'level': [
                    '6',
                    '13',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_NOHELL',
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_EXPL',
                        'AD_COLD',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_WHITE'
            },
            'flaming_sphere': {
                'name': 'flaming sphere',
                'symbol': 'S_EYE',
                'level': [
                    '6',
                    '13',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_EXPL',
                        'AD_FIRE',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'shocking_sphere': {
                'name': 'shocking sphere',
                'symbol': 'S_EYE',
                'level': [
                    '6',
                    '13',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_EXPL',
                        'AD_ELEC',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_ELEC'
                ],
                'resists_conveyed': [
                    'MR_ELEC'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_ZAP'
            },
            'beholder': {
                'name': 'beholder',
                'symbol': 'S_EYE',
                'level': [
                    '6',
                    '3',
                    '4',
                    '0',
                    '-10'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_GAZE',
                        'AD_SLOW',
                        '0',
                        '0'
                    ),
                    (
                        'AT_GAZE',
                        'AD_SLEE',
                        '2',
                        '25'
                    ),
                    (
                        'AT_GAZE',
                        'AD_DISN',
                        '0',
                        '0'
                    ),
                    (
                        'AT_GAZE',
                        'AD_STON',
                        '0',
                        '0'
                    ),
                    (
                        'AT_GAZE',
                        'AD_CNCL',
                        '2',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '10',
                    '10',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'kitten': {
                'name': 'kitten',
                'symbol': 'S_FELINE',
                'level': [
                    '2',
                    '18',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '150',
                    '150',
                    'MS_MEW',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'housecat': {
                'name': 'housecat',
                'symbol': 'S_FELINE',
                'level': [
                    '4',
                    '16',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '200',
                    '200',
                    'MS_MEW',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'jaguar': {
                'name': 'jaguar',
                'symbol': 'S_FELINE',
                'level': [
                    '4',
                    '15',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '600',
                    '300',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'lynx': {
                'name': 'lynx',
                'symbol': 'S_FELINE',
                'level': [
                    '5',
                    '15',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '10'
                    )
                ],
                'size': (
                    '600',
                    '300',
                    'MS_GROWL',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_CYAN'
            },
            'panther': {
                'name': 'panther',
                'symbol': 'S_FELINE',
                'level': [
                    '5',
                    '15',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '10'
                    )
                ],
                'size': (
                    '600',
                    '300',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLACK'
            },
            'large_cat': {
                'name': 'large cat',
                'symbol': 'S_FELINE',
                'level': [
                    '6',
                    '15',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '250',
                    '250',
                    'MS_MEW',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'tiger': {
                'name': 'tiger',
                'symbol': 'S_FELINE',
                'level': [
                    '6',
                    '12',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '10'
                    )
                ],
                'size': (
                    '600',
                    '300',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_YELLOW'
            },
            'gremlin': {
                'name': 'gremlin',
                'symbol': 'S_GREMLIN',
                'level': [
                    '5',
                    '12',
                    '2',
                    '25',
                    '-9'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_CURS',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '100',
                    '20',
                    'MS_LAUGH',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_STALK'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GREEN'
            },
            'gargoyle': {
                'name': 'gargoyle',
                'symbol': 'S_GREMLIN',
                'level': [
                    '6',
                    '10',
                    '-4',
                    '0',
                    '-9'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '1000',
                    '200',
                    'MS_GRUNT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_THICK_HIDE',
                    'M1_BREATHLESS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'winged_gargoyle': {
                'name': 'winged gargoyle',
                'symbol': 'S_GREMLIN',
                'level': [
                    '9',
                    '15',
                    '-2',
                    '0',
                    '-12'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    '1200',
                    '300',
                    'MS_GRUNT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_HUMANOID',
                    'M1_THICK_HIDE',
                    'M1_BREATHLESS',
                    'M1_OVIPAROUS'
                ],
                'flags2': [
                    'M2_LORD',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_LORD'
            },
            'hobbit': {
                'name': 'hobbit',
                'symbol': 'S_HUMANOID',
                'level': [
                    '1',
                    '9',
                    '10',
                    '0',
                    '6'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '500',
                    '200',
                    'MS_HUMANOID',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GREEN'
            },
            'dwarf': {
                'name': 'dwarf',
                'symbol': 'S_HUMANOID',
                'level': [
                    '2',
                    '6',
                    '10',
                    '10',
                    '4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '900',
                    '300',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_TUNNEL',
                    'M1_NEEDPICK',
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DWARF',
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'bugbear': {
                'name': 'bugbear',
                'symbol': 'S_HUMANOID',
                'level': [
                    '3',
                    '9',
                    '5',
                    '0',
                    '-6'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '1250',
                    '250',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'dwarf_lord': {
                'name': 'dwarf lord',
                'symbol': 'S_HUMANOID',
                'level': [
                    '4',
                    '6',
                    '10',
                    '10',
                    '5'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '900',
                    '300',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_TUNNEL',
                    'M1_NEEDPICK',
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_DWARF',
                    'M2_STRONG',
                    'M2_LORD',
                    'M2_MALE',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'dwarf_king': {
                'name': 'dwarf king',
                'symbol': 'S_HUMANOID',
                'level': [
                    '6',
                    '6',
                    '10',
                    '20',
                    '6'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '900',
                    '300',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_TUNNEL',
                    'M1_NEEDPICK',
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_DWARF',
                    'M2_STRONG',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'mind_flayer': {
                'name': 'mind flayer',
                'symbol': 'S_HUMANOID',
                'level': [
                    '9',
                    '12',
                    '5',
                    '90',
                    '-8'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_TENT',
                        'AD_DRIN',
                        '2',
                        '1'
                    ),
                    (
                        'AT_TENT',
                        'AD_DRIN',
                        '2',
                        '1'
                    ),
                    (
                        'AT_TENT',
                        'AD_DRIN',
                        '2',
                        '1'
                    )
                ],
                'size': (
                    '1450',
                    '400',
                    'MS_HISS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_MAGENTA'
            },
            'master_mind_flayer': {
                'name': 'master mind flayer',
                'symbol': 'S_HUMANOID',
                'level': [
                    '13',
                    '12',
                    '0',
                    '90',
                    '-8'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_TENT',
                        'AD_DRIN',
                        '2',
                        '1'
                    ),
                    (
                        'AT_TENT',
                        'AD_DRIN',
                        '2',
                        '1'
                    ),
                    (
                        'AT_TENT',
                        'AD_DRIN',
                        '2',
                        '1'
                    ),
                    (
                        'AT_TENT',
                        'AD_DRIN',
                        '2',
                        '1'
                    ),
                    (
                        'AT_TENT',
                        'AD_DRIN',
                        '2',
                        '1'
                    )
                ],
                'size': (
                    '1450',
                    '400',
                    'MS_HISS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_MAGENTA'
            },
            'manes': {
                'name': 'manes',
                'symbol': 'S_IMP',
                'level': [
                    '1',
                    '3',
                    '7',
                    '0',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_LGROUP',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '100',
                    '100',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STALK'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'homunculus': {
                'name': 'homunculus',
                'symbol': 'S_IMP',
                'level': [
                    '2',
                    '12',
                    '6',
                    '10',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_SLEE',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '60',
                    '100',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_STALK'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GREEN'
            },
            'imp': {
                'name': 'imp',
                'symbol': 'S_IMP',
                'level': [
                    '3',
                    '12',
                    '2',
                    '20',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '20',
                    '10',
                    'MS_CUSS',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_STALK'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'lemure': {
                'name': 'lemure',
                'symbol': 'S_IMP',
                'level': [
                    '3',
                    '3',
                    '7',
                    '0',
                    '-7'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    'G_LGROUP',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '150',
                    '100',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_WANDER',
                    'M2_STALK',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'quasit': {
                'name': 'quasit',
                'symbol': 'S_IMP',
                'level': [
                    '3',
                    '15',
                    '2',
                    '20',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_DRDX',
                        '1',
                        '2'
                    ),
                    (
                        'AT_CLAW',
                        'AD_DRDX',
                        '1',
                        '2'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '200',
                    '200',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_STALK'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'tengu': {
                'name': 'tengu',
                'symbol': 'S_IMP',
                'level': [
                    '6',
                    '13',
                    '5',
                    '30',
                    '7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '7'
                    )
                ],
                'size': (
                    '300',
                    '200',
                    'MS_SQAWK',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_TPORT',
                    'M1_TPORT_CNTRL'
                ],
                'flags2': [
                    'M2_STALK'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_CYAN'
            },
            'blue_jelly': {
                'name': 'blue jelly',
                'symbol': 'S_JELLY',
                'level': [
                    '4',
                    '0',
                    '8',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_COLD',
                        '0',
                        '6'
                    )
                ],
                'size': (
                    '50',
                    '20',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_COLD',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLUE'
            },
            'spotted_jelly': {
                'name': 'spotted jelly',
                'symbol': 'S_JELLY',
                'level': [
                    '5',
                    '0',
                    '8',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_ACID',
                        '0',
                        '6'
                    )
                ],
                'size': (
                    '50',
                    '20',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_ACID',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'ochre_jelly': {
                'name': 'ochre jelly',
                'symbol': 'S_JELLY',
                'level': [
                    '6',
                    '3',
                    '8',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_ACID',
                        '3',
                        '6'
                    ),
                    (
                        'AT_NONE',
                        'AD_ACID',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '50',
                    '20',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_ACID',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'kobold': {
                'name': 'kobold',
                'symbol': 'S_KOBOLD',
                'level': [
                    '0',
                    '6',
                    '10',
                    '0',
                    '-2'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '400',
                    '100',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'large_kobold': {
                'name': 'large kobold',
                'symbol': 'S_KOBOLD',
                'level': [
                    '1',
                    '6',
                    '10',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '450',
                    '150',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'kobold_lord': {
                'name': 'kobold lord',
                'symbol': 'S_KOBOLD',
                'level': [
                    '2',
                    '6',
                    '10',
                    '0',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '500',
                    '200',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_LORD',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'kobold_shaman': {
                'name': 'kobold shaman',
                'symbol': 'S_KOBOLD',
                'level': [
                    '2',
                    '6',
                    '6',
                    '10',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '450',
                    '150',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_ZAP'
            },
            'leprechaun': {
                'name': 'leprechaun',
                'symbol': 'S_LEPRECHAUN',
                'level': [
                    '5',
                    '15',
                    '8',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '4'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_SGLD',
                        '1',
                        '2'
                    )
                ],
                'size': (
                    '60',
                    '30',
                    'MS_LAUGH',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_TPORT'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_GREEDY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GREEN'
            },
            'small_mimic': {
                'name': 'small mimic',
                'symbol': 'S_MIMIC',
                'level': [
                    '7',
                    '3',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    '300',
                    '200',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_ACID'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_HIDE',
                    'M1_ANIMAL',
                    'M1_NOEYES',
                    'M1_NOHEAD',
                    'M1_NOLIMBS',
                    'M1_THICK_HIDE',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'large_mimic': {
                'name': 'large mimic',
                'symbol': 'S_MIMIC',
                'level': [
                    '8',
                    '3',
                    '7',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_STCK',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    '600',
                    '400',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_ACID'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_CLING',
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_HIDE',
                    'M1_ANIMAL',
                    'M1_NOEYES',
                    'M1_NOHEAD',
                    'M1_NOLIMBS',
                    'M1_THICK_HIDE',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_RED'
            },
            'giant_mimic': {
                'name': 'giant mimic',
                'symbol': 'S_MIMIC',
                'level': [
                    '9',
                    '3',
                    '7',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_STCK',
                        '3',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_STCK',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '800',
                    '500',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_ACID'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_CLING',
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_HIDE',
                    'M1_ANIMAL',
                    'M1_NOEYES',
                    'M1_NOHEAD',
                    'M1_NOLIMBS',
                    'M1_THICK_HIDE',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_LORD'
            },
            'wood_nymph': {
                'name': 'wood nymph',
                'symbol': 'S_NYMPH',
                'level': [
                    '3',
                    '12',
                    '9',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_SITM',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SEDU',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '600',
                    '300',
                    'MS_SEDUCE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_TPORT'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_FEMALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GREEN'
            },
            'water_nymph': {
                'name': 'water nymph',
                'symbol': 'S_NYMPH',
                'level': [
                    '3',
                    '12',
                    '9',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_SITM',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SEDU',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '600',
                    '300',
                    'MS_SEDUCE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_TPORT',
                    'M1_SWIM'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_FEMALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLUE'
            },
            'mountain_nymph': {
                'name': 'mountain nymph',
                'symbol': 'S_NYMPH',
                'level': [
                    '3',
                    '12',
                    '9',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_SITM',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SEDU',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '600',
                    '300',
                    'MS_SEDUCE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_TPORT'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_FEMALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'goblin': {
                'name': 'goblin',
                'symbol': 'S_ORC',
                'level': [
                    '0',
                    '6',
                    '10',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '400',
                    '100',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_ORC',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'hobgoblin': {
                'name': 'hobgoblin',
                'symbol': 'S_ORC',
                'level': [
                    '1',
                    '9',
                    '10',
                    '0',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1000',
                    '200',
                    'MS_ORC',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_ORC',
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'orc': {
                'name': 'orc',
                'symbol': 'S_ORC',
                'level': [
                    '1',
                    '9',
                    '10',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN',
                    'G_LGROUP'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '850',
                    '150',
                    'MS_ORC',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_ORC',
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'hill_orc': {
                'name': 'hill orc',
                'symbol': 'S_ORC',
                'level': [
                    '2',
                    '9',
                    '10',
                    '0',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_LGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1000',
                    '200',
                    'MS_ORC',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_ORC',
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_YELLOW'
            },
            'mordor_orc': {
                'name': 'Mordor orc',
                'symbol': 'S_ORC',
                'level': [
                    '3',
                    '5',
                    '10',
                    '0',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_LGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1200',
                    '200',
                    'MS_ORC',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_ORC',
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'uruk-hai': {
                'name': 'Uruk-hai',
                'symbol': 'S_ORC',
                'level': [
                    '3',
                    '7',
                    '10',
                    '0',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_LGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '1300',
                    '300',
                    'MS_ORC',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_ORC',
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLACK'
            },
            'orc_shaman': {
                'name': 'orc shaman',
                'symbol': 'S_ORC',
                'level': [
                    '3',
                    '9',
                    '5',
                    '10',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '1000',
                    '300',
                    'MS_ORC',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_ORC',
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_ZAP'
            },
            'orc-captain': {
                'name': 'orc-captain',
                'symbol': 'S_ORC',
                'level': [
                    '5',
                    '5',
                    '10',
                    '0',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '1350',
                    '350',
                    'MS_ORC',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_ORC',
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'rock_piercer': {
                'name': 'rock piercer',
                'symbol': 'S_PIERCER',
                'level': [
                    '3',
                    '1',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '4'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '200',
                    '200',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_CLING',
                    'M1_HIDE',
                    'M1_ANIMAL',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_CARNIVORE',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'iron_piercer': {
                'name': 'iron piercer',
                'symbol': 'S_PIERCER',
                'level': [
                    '5',
                    '1',
                    '0',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '400',
                    '300',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_CLING',
                    'M1_HIDE',
                    'M1_ANIMAL',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_CARNIVORE',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_CYAN'
            },
            'glass_piercer': {
                'name': 'glass piercer',
                'symbol': 'S_PIERCER',
                'level': [
                    '7',
                    '1',
                    '0',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '400',
                    '300',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_ACID'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_CLING',
                    'M1_HIDE',
                    'M1_ANIMAL',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_CARNIVORE',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_WHITE'
            },
            'rothe': {
                'name': 'rothe',
                'symbol': 'S_QUADRUPED',
                'level': [
                    '2',
                    '9',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '4'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '400',
                    '100',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'mumak': {
                'name': 'mumak',
                'symbol': 'S_QUADRUPED',
                'level': [
                    '5',
                    '9',
                    '0',
                    '0',
                    '-2'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BUTT',
                        'AD_PHYS',
                        '4',
                        '12'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '2500',
                    '500',
                    'MS_ROAR',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'leocrotta': {
                'name': 'leocrotta',
                'symbol': 'S_QUADRUPED',
                'level': [
                    '6',
                    '18',
                    '4',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1200',
                    '500',
                    'MS_IMITATE',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'wumpus': {
                'name': 'wumpus',
                'symbol': 'S_QUADRUPED',
                'level': [
                    '8',
                    '3',
                    '2',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '2500',
                    '500',
                    'MS_BURBLE',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_CLING',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_CYAN'
            },
            'titanothere': {
                'name': 'titanothere',
                'symbol': 'S_QUADRUPED',
                'level': [
                    '12',
                    '12',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '2650',
                    '650',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'baluchitherium': {
                'name': 'baluchitherium',
                'symbol': 'S_QUADRUPED',
                'level': [
                    '14',
                    '12',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '5',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '5',
                        '4'
                    )
                ],
                'size': (
                    '3800',
                    '800',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'mastodon': {
                'name': 'mastodon',
                'symbol': 'S_QUADRUPED',
                'level': [
                    '20',
                    '12',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BUTT',
                        'AD_PHYS',
                        '4',
                        '8'
                    ),
                    (
                        'AT_BUTT',
                        'AD_PHYS',
                        '4',
                        '8'
                    )
                ],
                'size': (
                    '3800',
                    '800',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLACK'
            },
            'sewer_rat': {
                'name': 'sewer rat',
                'symbol': 'S_RODENT',
                'level': [
                    '0',
                    '12',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '20',
                    '12',
                    'MS_SQEEK',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'giant_rat': {
                'name': 'giant rat',
                'symbol': 'S_RODENT',
                'level': [
                    '1',
                    '10',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '30',
                    '30',
                    'MS_SQEEK',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'rabid_rat': {
                'name': 'rabid rat',
                'symbol': 'S_RODENT',
                'level': [
                    '2',
                    '12',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRCO',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '30',
                    '5',
                    'MS_SQEEK',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_POIS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'wererat': {
                'name': 'wererat',
                'symbol': 'S_RODENT',
                'level': [
                    '2',
                    '12',
                    '6',
                    '10',
                    '-7'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_NOCORPSE'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_WERE',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '40',
                    '30',
                    'MS_SQEEK',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_NOHANDS',
                    'M1_POIS',
                    'M1_REGEN',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_WERE',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'rock_mole': {
                'name': 'rock mole',
                'symbol': 'S_RODENT',
                'level': [
                    '3',
                    '3',
                    '0',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '30',
                    '30',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_TUNNEL',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_METALLIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'woodchuck': {
                'name': 'woodchuck',
                'symbol': 'S_RODENT',
                'level': [
                    '3',
                    '3',
                    '0',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_GENO'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '30',
                    '30',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_TUNNEL/*LOGGING*/',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_SWIM',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    '/*Inreality'
                ],
                'flags3': [
                    'theytunnelinsteadofcuttinglumber.Oh'
                ],
                'color': 'CLR_BROWN'
            },
            'cave_spider': {
                'name': 'cave spider',
                'symbol': 'S_SPIDER',
                'level': [
                    '1',
                    '12',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '2'
                    )
                ],
                'size': (
                    '50',
                    '50',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_CONCEAL',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'centipede': {
                'name': 'centipede',
                'symbol': 'S_SPIDER',
                'level': [
                    '2',
                    '4',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '50',
                    '50',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_CONCEAL',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_YELLOW'
            },
            'giant_spider': {
                'name': 'giant spider',
                'symbol': 'S_SPIDER',
                'level': [
                    '5',
                    '15',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '100',
                    '100',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_POIS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_MAGENTA'
            },
            'scorpion': {
                'name': 'scorpion',
                'symbol': 'S_SPIDER',
                'level': [
                    '5',
                    '15',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '2'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '2'
                    ),
                    (
                        'AT_STNG',
                        'AD_DRST',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '50',
                    '100',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_CONCEAL',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_POIS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_RED'
            },
            'lurker_above': {
                'name': 'lurker above',
                'symbol': 'S_TRAPPER',
                'level': [
                    '10',
                    '3',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_DGST',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '800',
                    '350',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HIDE',
                    'M1_FLY',
                    'M1_ANIMAL',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STALK',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'trapper': {
                'name': 'trapper',
                'symbol': 'S_TRAPPER',
                'level': [
                    '12',
                    '3',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_DGST',
                        '1',
                        '10'
                    )
                ],
                'size': (
                    '800',
                    '350',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HIDE',
                    'M1_ANIMAL',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STALK',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'pony': {
                'name': 'pony',
                'symbol': 'S_UNICORN',
                'level': [
                    '3',
                    '16',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '2'
                    )
                ],
                'size': (
                    '1300',
                    '250',
                    'MS_NEIGH',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_STRONG',
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'white_unicorn': {
                'name': 'white unicorn',
                'symbol': 'S_UNICORN',
                'level': [
                    '4',
                    '24',
                    '2',
                    '70',
                    '7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BUTT',
                        'AD_PHYS',
                        '1',
                        '12'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1300',
                    '300',
                    'MS_NEIGH',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_STRONG',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_WHITE'
            },
            'gray_unicorn': {
                'name': 'gray unicorn',
                'symbol': 'S_UNICORN',
                'level': [
                    '4',
                    '24',
                    '2',
                    '70',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BUTT',
                        'AD_PHYS',
                        '1',
                        '12'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1300',
                    '300',
                    'MS_NEIGH',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_STRONG',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'black_unicorn': {
                'name': 'black unicorn',
                'symbol': 'S_UNICORN',
                'level': [
                    '4',
                    '24',
                    '2',
                    '70',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BUTT',
                        'AD_PHYS',
                        '1',
                        '12'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1300',
                    '300',
                    'MS_NEIGH',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_STRONG',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLACK'
            },
            'horse': {
                'name': 'horse',
                'symbol': 'S_UNICORN',
                'level': [
                    '5',
                    '20',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '1500',
                    '300',
                    'MS_NEIGH',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_STRONG',
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'warhorse': {
                'name': 'warhorse',
                'symbol': 'S_UNICORN',
                'level': [
                    '7',
                    '24',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '10'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '1800',
                    '350',
                    'MS_NEIGH',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_STRONG',
                    'M2_DOMESTIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'fog_cloud': {
                'name': 'fog cloud',
                'symbol': 'S_VORTEX',
                'level': [
                    '3',
                    '1',
                    '0',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_AMORPHOUS',
                    'M1_UNSOLID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'dust_vortex': {
                'name': 'dust vortex',
                'symbol': 'S_VORTEX',
                'level': [
                    '4',
                    '20',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_BLND',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'ice_vortex': {
                'name': 'ice vortex',
                'symbol': 'S_VORTEX',
                'level': [
                    '5',
                    '20',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_COLD',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_CYAN'
            },
            'energy_vortex': {
                'name': 'energy vortex',
                'symbol': 'S_VORTEX',
                'level': [
                    '6',
                    '20',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_ELEC',
                        '1',
                        '6'
                    ),
                    (
                        'AT_ENGL',
                        'AD_DREN',
                        '2',
                        '6'
                    ),
                    (
                        'AT_NONE',
                        'AD_ELEC',
                        '0',
                        '4'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_DISINT',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_UNSOLID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_ZAP'
            },
            'steam_vortex': {
                'name': 'steam vortex',
                'symbol': 'S_VORTEX',
                'level': [
                    '7',
                    '22',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    'G_NOCORPSE',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_FIRE',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_UNSOLID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLUE'
            },
            'fire_vortex': {
                'name': 'fire vortex',
                'symbol': 'S_VORTEX',
                'level': [
                    '8',
                    '22',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_FIRE',
                        '1',
                        '10'
                    ),
                    (
                        'AT_NONE',
                        'AD_FIRE',
                        '0',
                        '4'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_UNSOLID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_YELLOW'
            },
            'baby_long_worm': {
                'name': 'baby long worm',
                'symbol': 'S_WORM, LVL(5, 3, 5, 0, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 1, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(600, 250, MS_SILENT, MZ_LARGE), 0, 0,\n         M1_ANIMAL | M1_SLITHY | M1_NOLIMBS | M1_CARNIVORE | M1_NOTAKE,\n         M2_HOSTILE, 0, CLR_BROWN),\n     MON("baby purple worm", S_WORM, LVL(8, 3, 5, 0, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 1, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(600, 250, MS_SILENT, MZ_LARGE), 0, 0,\n         M1_ANIMAL | M1_SLITHY | M1_NOLIMBS | M1_CARNIVORE, M2_HOSTILE, 0,\n         CLR_MAGENTA),\n     MON("long worm", S_WORM',
                'level': [
                    '9',
                    '3',
                    '5',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '1500',
                    '500',
                    'MS_SILENT',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_NOLIMBS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'purple_worm': {
                'name': 'purple worm',
                'symbol': 'S_WORM',
                'level': [
                    '15',
                    '9',
                    '6',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_ENGL',
                        'AD_DGST',
                        '1',
                        '10'
                    )
                ],
                'size': (
                    '2700',
                    '700',
                    'MS_SILENT',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_NOLIMBS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_MAGENTA'
            },
            'grid_bug': {
                'name': 'grid bug',
                'symbol': 'S_XAN',
                'level': [
                    '0',
                    '12',
                    '9',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    'G_NOCORPSE',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_ELEC',
                        '1',
                        '1'
                    )
                ],
                'size': (
                    '15',
                    '10',
                    'MS_BUZZ',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_ELEC',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_MAGENTA'
            },
            'xan': {
                'name': 'xan',
                'symbol': 'S_XAN',
                'level': [
                    '7',
                    '18',
                    '-4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_STNG',
                        'AD_LEGS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '300',
                    '300',
                    'MS_BUZZ',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'yellow_light': {
                'name': 'yellow light',
                'symbol': 'S_LIGHT',
                'level': [
                    '3',
                    '15',
                    '0',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_GENO',
                    '4'
                ),
                'attacks': [
                    (
                        'AT_EXPL',
                        'AD_BLND',
                        '10',
                        '20'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_DISINT',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_UNSOLID',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_YELLOW'
            },
            'black_light': {
                'name': 'black light',
                'symbol': 'S_LIGHT',
                'level': [
                    '5',
                    '15',
                    '0',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_EXPL',
                        'AD_HALU',
                        '10',
                        '12'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_DISINT',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_UNSOLID',
                    'M1_SEE_INVIS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLACK'
            },
            'zruty': {
                'name': 'zruty',
                'symbol': 'S_ZRUTY',
                'level': [
                    '9',
                    '8',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '1200',
                    '600',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'couatl': {
                'name': 'couatl',
                'symbol': 'S_ANGEL',
                'level': [
                    '8',
                    '10',
                    '5',
                    '30',
                    '7'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_SGROUP',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '2',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_HUGS',
                        'AD_WRAP',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '900',
                    '400',
                    'MS_HISS',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_NOHANDS',
                    'M1_SLITHY',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_MINION',
                    'M2_STALK',
                    'M2_STRONG',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GREEN'
            },
            'aleax': {
                'name': 'Aleax',
                'symbol': 'S_ANGEL',
                'level': [
                    '10',
                    '8',
                    '0',
                    '30',
                    '7'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_IMITATE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_MINION',
                    'M2_STALK',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_YELLOW'
            },
            'angel': {
                'name': 'Angel',
                'symbol': 'S_ANGEL',
                'level': [
                    '14',
                    '10',
                    '-4',
                    '55',
                    '12'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_MAGC',
                        'AD_MAGM',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_CUSS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_HUMANOID',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_MINION',
                    'M2_STALK',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_WHITE'
            },
            'ki-rin': {
                'name': 'ki-rin',
                'symbol': 'S_ANGEL',
                'level': [
                    '16',
                    '18',
                    '-5',
                    '90',
                    '15'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_BUTT',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NEIGH',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_MINION',
                    'M2_STALK',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_LORD'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_GOLD'
            },
            'archon': {
                'name': 'Archon',
                'symbol': 'S_ANGEL',
                'level': [
                    '19',
                    '16',
                    '-6',
                    '80',
                    '15'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_GAZE',
                        'AD_BLND',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_CUSS',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_HUMANOID',
                    'M1_SEE_INVIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_MINION',
                    'M2_STALK',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_LORD',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'bat': {
                'name': 'bat',
                'symbol': 'S_BAT',
                'level': [
                    '0',
                    '22',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '20',
                    '20',
                    'MS_SQEEK',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_WANDER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'giant_bat': {
                'name': 'giant bat',
                'symbol': 'S_BAT',
                'level': [
                    '2',
                    '22',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '30',
                    '30',
                    'MS_SQEEK',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'raven': {
                'name': 'raven',
                'symbol': 'S_BAT',
                'level': [
                    '4',
                    '20',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_BLND',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '40',
                    '20',
                    'MS_SQAWK',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLACK'
            },
            'vampire_bat': {
                'name': 'vampire bat',
                'symbol': 'S_BAT',
                'level': [
                    '5',
                    '20',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '30',
                    '20',
                    'MS_SQEEK',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_POIS',
                    'M1_REGEN',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLACK'
            },
            'plains_centaur': {
                'name': 'plains centaur',
                'symbol': 'S_CENTAUR',
                'level': [
                    '4',
                    '18',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '2500',
                    '500',
                    'MS_HUMANOID',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'forest_centaur': {
                'name': 'forest centaur',
                'symbol': 'S_CENTAUR',
                'level': [
                    '5',
                    '18',
                    '3',
                    '10',
                    '-1'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '2550',
                    '600',
                    'MS_HUMANOID',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GREEN'
            },
            'mountain_centaur': {
                'name': 'mountain centaur',
                'symbol': 'S_CENTAUR',
                'level': [
                    '6',
                    '20',
                    '2',
                    '10',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '10'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '2550',
                    '500',
                    'MS_HUMANOID',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_CYAN'
            },
            'baby_gray_dragon': {
                'name': 'baby gray dragon',
                'symbol': 'S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), 0, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, CLR_GRAY),\n     MON("baby silver dragon", S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), 0, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, DRAGON_SILVER),\n #if 0 /* DEFERRED */\n     MON("baby shimmering dragon", S_DRAGON,\n         LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6),\n           NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), 0, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, CLR_CYAN),\n #endif\n     MON("baby red dragon", S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), MR_FIRE, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, M3_INFRAVISIBLE,\n         CLR_RED),\n     MON("baby white dragon", S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), MR_COLD, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, CLR_WHITE),\n     MON("baby orange dragon", S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), MR_SLEEP, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, CLR_ORANGE),\n     MON("baby black dragon", S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), MR_DISINT, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, CLR_BLACK),\n     MON("baby blue dragon", S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), MR_ELEC, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, CLR_BLUE),\n     MON("baby green dragon", S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), MR_POISON, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE | M1_POIS,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, CLR_GREEN),\n     MON("baby yellow dragon", S_DRAGON, LVL(12, 9, 2, 10, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 2, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(1500, 500, MS_ROAR, MZ_HUGE), MR_ACID | MR_STONE, 0,\n         M1_FLY | M1_THICK_HIDE | M1_NOHANDS | M1_CARNIVORE | M1_ACID,\n         M2_HOSTILE | M2_STRONG | M2_GREEDY | M2_JEWELS, 0, CLR_YELLOW),\n     MON("gray dragon", S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_MAGM',
                        '4',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'silver_dragon': {
                'name': 'silver dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_COLD',
                        '4',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'DRAGON_SILVER'
            },
            'shimmering_dragon': {
                'name': 'shimmering dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_MAGM',
                        '4',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_CYAN'
            },
            'red_dragon': {
                'name': 'red dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_FIRE',
                        '6',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'white_dragon': {
                'name': 'white dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_COLD',
                        '4',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_WHITE'
            },
            'orange_dragon': {
                'name': 'orange dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '5'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_SLEE',
                        '4',
                        '25'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_ORANGE'
            },
            'black_dragon': {
                'name': 'black dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '-6'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_DISN',
                        '1',
                        '255'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_DISINT'
                ],
                'resists_conveyed': [
                    'MR_DISINT'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLACK'
            },
            'blue_dragon': {
                'name': 'blue dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_ELEC',
                        '4',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_ELEC'
                ],
                'resists_conveyed': [
                    'MR_ELEC'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLUE'
            },
            'green_dragon': {
                'name': 'green dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '6'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_DRST',
                        '4',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'yellow_dragon': {
                'name': 'yellow dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '9',
                    '-1',
                    '20',
                    '7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_ACID',
                        '4',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1500',
                    'MS_ROAR',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_SEE_INVIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE',
                    'M1_ACID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_YELLOW'
            },
            'stalker': {
                'name': 'stalker',
                'symbol': 'S_ELEMENTAL',
                'level': [
                    '8',
                    '12',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '4',
                        '4'
                    )
                ],
                'size': (
                    '900',
                    '400',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_FLY',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_WANDER',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_WHITE'
            },
            'air_elemental': {
                'name': 'air elemental',
                'symbol': 'S_ELEMENTAL',
                'level': [
                    '8',
                    '36',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_PHYS',
                        '1',
                        '10'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_BREATHLESS',
                    'M1_UNSOLID',
                    'M1_FLY'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_CYAN'
            },
            'fire_elemental': {
                'name': 'fire elemental',
                'symbol': 'S_ELEMENTAL',
                'level': [
                    '8',
                    '12',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_FIRE',
                        '3',
                        '6'
                    ),
                    (
                        'AT_NONE',
                        'AD_FIRE',
                        '0',
                        '4'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_BREATHLESS',
                    'M1_UNSOLID',
                    'M1_FLY',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_YELLOW'
            },
            'earth_elemental': {
                'name': 'earth elemental',
                'symbol': 'S_ELEMENTAL',
                'level': [
                    '8',
                    '6',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '2500',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_BREATHLESS',
                    'M1_WALLWALK',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'water_elemental': {
                'name': 'water elemental',
                'symbol': 'S_ELEMENTAL',
                'level': [
                    '8',
                    '6',
                    '2',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '5',
                        '6'
                    )
                ],
                'size': (
                    '2500',
                    '0',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_BREATHLESS',
                    'M1_UNSOLID',
                    'M1_AMPHIBIOUS',
                    'M1_SWIM'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLUE'
            },
            'lichen': {
                'name': 'lichen',
                'symbol': 'S_FUNGUS',
                'level': [
                    '0',
                    '1',
                    '9',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '4'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_STCK',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '20',
                    '200',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BRIGHT_GREEN'
            },
            'brown_mold': {
                'name': 'brown mold',
                'symbol': 'S_FUNGUS',
                'level': [
                    '1',
                    '0',
                    '9',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_COLD',
                        '0',
                        '6'
                    )
                ],
                'size': (
                    '50',
                    '30',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_COLD',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'yellow_mold': {
                'name': 'yellow mold',
                'symbol': 'S_FUNGUS',
                'level': [
                    '1',
                    '0',
                    '9',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_STUN',
                        '0',
                        '4'
                    )
                ],
                'size': (
                    '50',
                    '30',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_POIS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_YELLOW'
            },
            'green_mold': {
                'name': 'green mold',
                'symbol': 'S_FUNGUS',
                'level': [
                    '1',
                    '0',
                    '9',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_ACID',
                        '0',
                        '4'
                    )
                ],
                'size': (
                    '50',
                    '30',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_ACID',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'red_mold': {
                'name': 'red mold',
                'symbol': 'S_FUNGUS',
                'level': [
                    '1',
                    '0',
                    '9',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_FIRE',
                        '0',
                        '4'
                    )
                ],
                'size': (
                    '50',
                    '30',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'shrieker': {
                'name': 'shrieker',
                'symbol': 'S_FUNGUS',
                'level': [
                    '3',
                    '1',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [],
                'size': (
                    '100',
                    '100',
                    'MS_SHRIEK',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_MAGENTA'
            },
            'violet_fungus': {
                'name': 'violet fungus',
                'symbol': 'S_FUNGUS',
                'level': [
                    '3',
                    '1',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_TUCH',
                        'AD_STCK',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '100',
                    '100',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_MAGENTA'
            },
            'gnome': {
                'name': 'gnome',
                'symbol': 'S_GNOME',
                'level': [
                    '1',
                    '6',
                    '10',
                    '4',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '650',
                    '100',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_GNOME',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'gnome_lord': {
                'name': 'gnome lord',
                'symbol': 'S_GNOME',
                'level': [
                    '3',
                    '8',
                    '10',
                    '4',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '700',
                    '120',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_GNOME',
                    'M2_LORD',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'gnomish_wizard': {
                'name': 'gnomish wizard',
                'symbol': 'S_GNOME',
                'level': [
                    '3',
                    '10',
                    '4',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '700',
                    '120',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_GNOME',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_ZAP'
            },
            'gnome_king': {
                'name': 'gnome king',
                'symbol': 'S_GNOME',
                'level': [
                    '5',
                    '10',
                    '10',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '750',
                    '150',
                    'MS_ORC',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_GNOME',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'giant': {
                'name': 'giant',
                'symbol': 'S_GIANT',
                'level': [
                    '6',
                    '6',
                    '0',
                    '0',
                    '2'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '10'
                    )
                ],
                'size': (
                    '2250',
                    '750',
                    'MS_BOAST',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_GIANT',
                    'M2_STRONG',
                    'M2_ROCKTHROW',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'stone_giant': {
                'name': 'stone giant',
                'symbol': 'S_GIANT',
                'level': [
                    '6',
                    '6',
                    '0',
                    '0',
                    '2'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '10'
                    )
                ],
                'size': (
                    '2250',
                    '750',
                    'MS_BOAST',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_GIANT',
                    'M2_STRONG',
                    'M2_ROCKTHROW',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'hill_giant': {
                'name': 'hill giant',
                'symbol': 'S_GIANT',
                'level': [
                    '8',
                    '10',
                    '6',
                    '0',
                    '-2'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '2200',
                    '700',
                    'MS_BOAST',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_GIANT',
                    'M2_STRONG',
                    'M2_ROCKTHROW',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_CYAN'
            },
            'fire_giant': {
                'name': 'fire giant',
                'symbol': 'S_GIANT',
                'level': [
                    '9',
                    '12',
                    '4',
                    '5',
                    '2'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '10'
                    )
                ],
                'size': (
                    '2250',
                    '750',
                    'MS_BOAST',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_GIANT',
                    'M2_STRONG',
                    'M2_ROCKTHROW',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_YELLOW'
            },
            'frost_giant': {
                'name': 'frost giant',
                'symbol': 'S_GIANT',
                'level': [
                    '10',
                    '12',
                    '3',
                    '10',
                    '-3'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '12'
                    )
                ],
                'size': (
                    '2250',
                    '750',
                    'MS_BOAST',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_GIANT',
                    'M2_STRONG',
                    'M2_ROCKTHROW',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_WHITE'
            },
            'ettin': {
                'name': 'ettin',
                'symbol': 'S_GIANT',
                'level': [
                    '10',
                    '12',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '1700',
                    '500',
                    'MS_GRUNT',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'storm_giant': {
                'name': 'storm giant',
                'symbol': 'S_GIANT',
                'level': [
                    '16',
                    '12',
                    '3',
                    '10',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '12'
                    )
                ],
                'size': (
                    '2250',
                    '750',
                    'MS_BOAST',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_ELEC'
                ],
                'resists_conveyed': [
                    'MR_ELEC'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_GIANT',
                    'M2_STRONG',
                    'M2_ROCKTHROW',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'titan': {
                'name': 'titan',
                'symbol': 'S_GIANT',
                'level': [
                    '16',
                    '18',
                    '-3',
                    '70',
                    '9'
                ],
                'gen_flags': (
                    '1',
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '2300',
                    '900',
                    'MS_SPELL',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_ROCKTHROW',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_MAGENTA'
            },
            'minotaur': {
                'name': 'minotaur',
                'symbol': 'S_GIANT',
                'level': [
                    '15',
                    '15',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '10'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '10'
                    ),
                    (
                        'AT_BUTT',
                        'AD_PHYS',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '1500',
                    '700',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'jabberwock': {
                'name': 'jabberwock',
                'symbol': 'S_JABBERWOCK',
                'level': [
                    '15',
                    '12',
                    '-2',
                    '50',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '10'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '10'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '10'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '10'
                    )
                ],
                'size': (
                    '1300',
                    '600',
                    'MS_BURBLE',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_FLY',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_ORANGE'
            },
            'vorpal_jabberwock': {
                'name': 'vorpal jabberwock',
                'symbol': 'S_JABBERWOCK',
                'level': [
                    '20',
                    '12',
                    '-2',
                    '50',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '10'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '10'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '10'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '10'
                    )
                ],
                'size': (
                    '1300',
                    '600',
                    'MS_BURBLE',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_FLY',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'keystone_kop': {
                'name': 'Keystone Kop',
                'symbol': 'S_KOP',
                'level': [
                    '1',
                    '6',
                    '10',
                    '10',
                    '9'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_LGROUP',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '200',
                    'MS_ARREST',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HUMAN',
                    'M2_WANDER',
                    'M2_HOSTILE',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLUE'
            },
            'kop_sergeant': {
                'name': 'Kop Sergeant',
                'symbol': 'S_KOP',
                'level': [
                    '2',
                    '8',
                    '10',
                    '10',
                    '10'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '200',
                    'MS_ARREST',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HUMAN',
                    'M2_WANDER',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLUE'
            },
            'kop_lieutenant': {
                'name': 'Kop Lieutenant',
                'symbol': 'S_KOP',
                'level': [
                    '3',
                    '10',
                    '10',
                    '20',
                    '11'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '200',
                    'MS_ARREST',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HUMAN',
                    'M2_WANDER',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_CYAN'
            },
            'kop_kaptain': {
                'name': 'Kop Kaptain',
                'symbol': 'S_KOP',
                'level': [
                    '4',
                    '12',
                    '10',
                    '20',
                    '12'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '200',
                    'MS_ARREST',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HUMAN',
                    'M2_WANDER',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'lich': {
                'name': 'lich',
                'symbol': 'S_LICH',
                'level': [
                    '11',
                    '6',
                    '0',
                    '30',
                    '-9'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_COLD',
                        '1',
                        '10'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '1200',
                    '100',
                    'MS_MUMBLE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'demilich': {
                'name': 'demilich',
                'symbol': 'S_LICH',
                'level': [
                    '14',
                    '9',
                    '-2',
                    '60',
                    '-12'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_COLD',
                        '3',
                        '4'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '1200',
                    '100',
                    'MS_MUMBLE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'master_lich': {
                'name': 'master lich',
                'symbol': 'S_LICH',
                'level': [
                    '17',
                    '9',
                    '-4',
                    '90',
                    '-15'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_COLD',
                        '3',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '1200',
                    '100',
                    'MS_MUMBLE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSBOOK',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'arch-lich': {
                'name': 'arch-lich',
                'symbol': 'S_LICH',
                'level': [
                    '25',
                    '9',
                    '-6',
                    '90',
                    '-15'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_COLD',
                        '5',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '1200',
                    '100',
                    'MS_MUMBLE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_ELEC',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSBOOK',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'kobold_mummy': {
                'name': 'kobold mummy',
                'symbol': 'S_MUMMY',
                'level': [
                    '3',
                    '8',
                    '6',
                    '20',
                    '-2'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '400',
                    '50',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'gnome_mummy': {
                'name': 'gnome mummy',
                'symbol': 'S_MUMMY',
                'level': [
                    '4',
                    '10',
                    '6',
                    '20',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '650',
                    '50',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_GNOME'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'orc_mummy': {
                'name': 'orc mummy',
                'symbol': 'S_MUMMY',
                'level': [
                    '5',
                    '10',
                    '5',
                    '20',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '850',
                    '75',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_ORC',
                    'M2_GREEDY',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'dwarf_mummy': {
                'name': 'dwarf mummy',
                'symbol': 'S_MUMMY',
                'level': [
                    '5',
                    '10',
                    '5',
                    '20',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '900',
                    '150',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_DWARF',
                    'M2_GREEDY',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'elf_mummy': {
                'name': 'elf mummy',
                'symbol': 'S_MUMMY',
                'level': [
                    '6',
                    '12',
                    '4',
                    '30',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '175',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_ELF'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GREEN'
            },
            'human_mummy': {
                'name': 'human mummy',
                'symbol': 'S_MUMMY',
                'level': [
                    '6',
                    '12',
                    '4',
                    '30',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '200',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'ettin_mummy': {
                'name': 'ettin mummy',
                'symbol': 'S_MUMMY',
                'level': [
                    '7',
                    '12',
                    '4',
                    '30',
                    '-6'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1700',
                    '250',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'giant_mummy': {
                'name': 'giant mummy',
                'symbol': 'S_MUMMY',
                'level': [
                    '8',
                    '14',
                    '3',
                    '30',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    '2050',
                    '375',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_HOSTILE',
                    'M2_GIANT',
                    'M2_STRONG',
                    'M2_JEWELS'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_CYAN'
            },
            'red_naga_hatchling': {
                'name': 'red naga hatchling',
                'symbol': 'S_NAGA, LVL(3, 10, 6, 0, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 1, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(500, 100, MS_MUMBLE, MZ_LARGE), MR_FIRE | MR_POISON,\n         MR_FIRE | MR_POISON,\n         M1_NOLIMBS | M1_SLITHY | M1_THICK_HIDE | M1_NOTAKE | M1_OMNIVORE,\n         M2_STRONG, M3_INFRAVISIBLE, CLR_RED),\n     MON("black naga hatchling", S_NAGA, LVL(3, 10, 6, 0, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 1, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(500, 100, MS_MUMBLE, MZ_LARGE), MR_POISON | MR_ACID | MR_STONE,\n         MR_POISON | MR_STONE, M1_NOLIMBS | M1_SLITHY | M1_THICK_HIDE | M1_ACID\n                                   | M1_NOTAKE | M1_CARNIVORE,\n         M2_STRONG, 0, CLR_BLACK),\n     MON("golden naga hatchling", S_NAGA, LVL(3, 10, 6, 0, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 1, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(500, 100, MS_MUMBLE, MZ_LARGE), MR_POISON, MR_POISON,\n         M1_NOLIMBS | M1_SLITHY | M1_THICK_HIDE | M1_NOTAKE | M1_OMNIVORE,\n         M2_STRONG, 0, HI_GOLD),\n     MON("guardian naga hatchling", S_NAGA, LVL(3, 10, 6, 0, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 1, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(500, 100, MS_MUMBLE, MZ_LARGE), MR_POISON, MR_POISON,\n         M1_NOLIMBS | M1_SLITHY | M1_THICK_HIDE | M1_NOTAKE | M1_OMNIVORE,\n         M2_STRONG, 0, CLR_GREEN),\n     MON("red naga", S_NAGA',
                'level': [
                    '6',
                    '12',
                    '4',
                    '0',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_BREA',
                        'AD_FIRE',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '2600',
                    '400',
                    'MS_MUMBLE',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_NOLIMBS',
                    'M1_SLITHY',
                    'M1_THICK_HIDE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'black_naga': {
                'name': 'black naga',
                'symbol': 'S_NAGA',
                'level': [
                    '8',
                    '14',
                    '2',
                    '10',
                    '4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_SPIT',
                        'AD_ACID',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '2600',
                    '400',
                    'MS_MUMBLE',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_NOLIMBS',
                    'M1_SLITHY',
                    'M1_THICK_HIDE',
                    'M1_OVIPAROUS',
                    'M1_ACID',
                    'M1_NOTAKE',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLACK'
            },
            'golden_naga': {
                'name': 'golden naga',
                'symbol': 'S_NAGA',
                'level': [
                    '10',
                    '14',
                    '2',
                    '70',
                    '5'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '2600',
                    '400',
                    'MS_MUMBLE',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_NOLIMBS',
                    'M1_SLITHY',
                    'M1_THICK_HIDE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_GOLD'
            },
            'guardian_naga': {
                'name': 'guardian naga',
                'symbol': 'S_NAGA',
                'level': [
                    '12',
                    '16',
                    '0',
                    '50',
                    '7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PLYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_SPIT',
                        'AD_DRST',
                        '1',
                        '6'
                    ),
                    (
                        'AT_HUGS',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '2600',
                    '400',
                    'MS_MUMBLE',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_NOLIMBS',
                    'M1_SLITHY',
                    'M1_THICK_HIDE',
                    'M1_OVIPAROUS',
                    'M1_POIS',
                    'M1_NOTAKE',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'ogre': {
                'name': 'ogre',
                'symbol': 'S_OGRE',
                'level': [
                    '5',
                    '10',
                    '5',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_SGROUP',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '5'
                    )
                ],
                'size': (
                    '1600',
                    '500',
                    'MS_GRUNT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'ogre_lord': {
                'name': 'ogre lord',
                'symbol': 'S_OGRE',
                'level': [
                    '7',
                    '12',
                    '3',
                    '30',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1700',
                    '700',
                    'MS_GRUNT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_LORD',
                    'M2_MALE',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'ogre_king': {
                'name': 'ogre king',
                'symbol': 'S_OGRE',
                'level': [
                    '9',
                    '14',
                    '4',
                    '60',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '5'
                    )
                ],
                'size': (
                    '1700',
                    '750',
                    'MS_GRUNT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'gray_ooze': {
                'name': 'gray ooze',
                'symbol': 'S_PUDDING',
                'level': [
                    '3',
                    '1',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_RUST',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '500',
                    '250',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_OMNIVORE',
                    'M1_ACID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'brown_pudding': {
                'name': 'brown pudding',
                'symbol': 'S_PUDDING',
                'level': [
                    '5',
                    '3',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DCAY',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '500',
                    '250',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_OMNIVORE',
                    'M1_ACID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'green_slime': {
                'name': 'green slime',
                'symbol': 'S_PUDDING',
                'level': [
                    '6',
                    '6',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_SLIM',
                        '1',
                        '4'
                    ),
                    (
                        'AT_NONE',
                        'AD_SLIM',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '400',
                    '150',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_OMNIVORE',
                    'M1_ACID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'black_pudding': {
                'name': 'black pudding',
                'symbol': 'S_PUDDING',
                'level': [
                    '10',
                    '6',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_CORR',
                        '3',
                        '8'
                    ),
                    (
                        'AT_NONE',
                        'AD_CORR',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '900',
                    '250',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_AMORPHOUS',
                    'M1_NOEYES',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_MINDLESS',
                    'M1_OMNIVORE',
                    'M1_ACID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLACK'
            },
            'quantum_mechanic': {
                'name': 'quantum mechanic',
                'symbol': 'S_QUANTMECH',
                'level': [
                    '7',
                    '12',
                    '3',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_TLPT',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '20',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE',
                    'M1_POIS',
                    'M1_TPORT'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_CYAN'
            },
            'rust_monster': {
                'name': 'rust monster',
                'symbol': 'S_RUSTMONST',
                'level': [
                    '5',
                    '18',
                    '2',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_RUST',
                        '0',
                        '0'
                    ),
                    (
                        'AT_TUCH',
                        'AD_RUST',
                        '0',
                        '0'
                    ),
                    (
                        'AT_NONE',
                        'AD_RUST',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '1000',
                    '250',
                    'MS_SILENT',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_METALLIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'disenchanter': {
                'name': 'disenchanter',
                'symbol': 'S_RUSTMONST',
                'level': [
                    '12',
                    '12',
                    '-10',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_ENCH',
                        '4',
                        '4'
                    ),
                    (
                        'AT_NONE',
                        'AD_ENCH',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '750',
                    '200',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLUE'
            },
            'garter_snake': {
                'name': 'garter snake',
                'symbol': 'S_SNAKE',
                'level': [
                    '1',
                    '8',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_LGROUP',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '2'
                    )
                ],
                'size': (
                    '50',
                    '60',
                    'MS_HISS',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_CONCEAL',
                    'M1_NOLIMBS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    '0'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'snake': {
                'name': 'snake',
                'symbol': 'S_SNAKE',
                'level': [
                    '4',
                    '15',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '100',
                    '80',
                    'MS_HISS',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_CONCEAL',
                    'M1_NOLIMBS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_POIS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'water_moccasin': {
                'name': 'water moccasin',
                'symbol': 'S_SNAKE',
                'level': [
                    '4',
                    '15',
                    '3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN',
                    'G_LGROUP'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '150',
                    '80',
                    'MS_HISS',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_CONCEAL',
                    'M1_NOLIMBS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_POIS',
                    'M1_CARNIVORE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_RED'
            },
            'python': {
                'name': 'python',
                'symbol': 'S_SNAKE',
                'level': [
                    '6',
                    '3',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_TUCH',
                        'AD_PHYS',
                        '0',
                        '0'
                    ),
                    (
                        'AT_HUGS',
                        'AD_WRAP',
                        '1',
                        '4'
                    ),
                    (
                        'AT_HUGS',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '250',
                    '100',
                    'MS_HISS',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_NOLIMBS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_CARNIVORE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_MAGENTA'
            },
            'pit_viper': {
                'name': 'pit viper',
                'symbol': 'S_SNAKE',
                'level': [
                    '6',
                    '15',
                    '2',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '1',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '100',
                    '60',
                    'MS_HISS',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_CONCEAL',
                    'M1_NOLIMBS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_POIS',
                    'M1_CARNIVORE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'cobra': {
                'name': 'cobra',
                'symbol': 'S_SNAKE',
                'level': [
                    '6',
                    '18',
                    '2',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '2',
                        '4'
                    ),
                    (
                        'AT_SPIT',
                        'AD_BLND',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '250',
                    '100',
                    'MS_HISS',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_CONCEAL',
                    'M1_NOLIMBS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_POIS',
                    'M1_CARNIVORE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLUE'
            },
            'troll': {
                'name': 'troll',
                'symbol': 'S_TROLL',
                'level': [
                    '7',
                    '12',
                    '4',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '2'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '4',
                        '2'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '800',
                    '350',
                    'MS_GRUNT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'ice_troll': {
                'name': 'ice troll',
                'symbol': 'S_TROLL',
                'level': [
                    '9',
                    '10',
                    '2',
                    '20',
                    '-3'
                ],
                'gen_flags': (
                    'G_NOHELL',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_COLD',
                        '2',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1000',
                    '300',
                    'MS_GRUNT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_WHITE'
            },
            'rock_troll': {
                'name': 'rock troll',
                'symbol': 'S_TROLL',
                'level': [
                    '9',
                    '12',
                    '0',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1200',
                    '300',
                    'MS_GRUNT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_CYAN'
            },
            'water_troll': {
                'name': 'water troll',
                'symbol': 'S_TROLL',
                'level': [
                    '11',
                    '14',
                    '4',
                    '40',
                    '-3'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_GENO'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1200',
                    '350',
                    'MS_GRUNT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_CARNIVORE',
                    'M1_SWIM'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'olog-hai': {
                'name': 'Olog-hai',
                'symbol': 'S_TROLL',
                'level': [
                    '13',
                    '12',
                    '-4',
                    '0',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1500',
                    '400',
                    'MS_GRUNT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'umber_hulk': {
                'name': 'umber hulk',
                'symbol': 'S_UMBER',
                'level': [
                    '9',
                    '6',
                    '2',
                    '25',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '5'
                    ),
                    (
                        'AT_GAZE',
                        'AD_CONF',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '1200',
                    '500',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_TUNNEL',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'vampire': {
                'name': 'vampire',
                'symbol': 'S_VAMPIRE',
                'level': [
                    '10',
                    '12',
                    '1',
                    '25',
                    '-8'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_DRLI',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_VAMPIRE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_SHAPESHIFTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'vampire_lord': {
                'name': 'vampire lord',
                'symbol': 'S_VAMPIRE',
                'level': [
                    '12',
                    '14',
                    '0',
                    '50',
                    '-9'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_DRLI',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_VAMPIRE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_LORD',
                    'M2_MALE',
                    'M2_SHAPESHIFTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLUE'
            },
            'vampire_mage': {
                'name': 'vampire mage',
                'symbol': 'S_VAMPIRE',
                'level': [
                    '20',
                    '14',
                    '-4',
                    '50',
                    '-9'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_DRLI',
                        '2',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_DRLI',
                        '1',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_VAMPIRE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_LORD',
                    'M2_MALE',
                    'M2_MAGIC',
                    'M2_SHAPESHIFTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_ZAP'
            },
            'vlad_the_impaler': {
                'name': 'Vlad the Impaler',
                'symbol': 'S_VAMPIRE',
                'level': [
                    '28',
                    '26',
                    '-6',
                    '80',
                    '-10'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_NOCORPSE',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '10'
                    ),
                    (
                        'AT_BITE',
                        'AD_DRLI',
                        '1',
                        '12'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_VAMPIRE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_SHAPESHIFTER'
                ],
                'flags3': [
                    'M3_WAITFORU',
                    'M3_WANTSCAND',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'barrow_wight': {
                'name': 'barrow wight',
                'symbol': 'S_WRAITH',
                'level': [
                    '3',
                    '12',
                    '5',
                    '5',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_DRLI',
                        '0',
                        '0'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '1200',
                    '0',
                    'MS_SPELL',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'wraith': {
                'name': 'wraith',
                'symbol': 'S_WRAITH',
                'level': [
                    '6',
                    '12',
                    '4',
                    '15',
                    '-6'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_DRLI',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '0',
                    '0',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_FLY',
                    'M1_HUMANOID',
                    'M1_UNSOLID'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLACK'
            },
            'nazgul': {
                'name': 'Nazgul',
                'symbol': 'S_WRAITH',
                'level': [
                    '13',
                    '12',
                    '0',
                    '25',
                    '-17'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_DRLI',
                        '1',
                        '4'
                    ),
                    (
                        'AT_BREA',
                        'AD_SLEE',
                        '2',
                        '25'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '0',
                    'MS_SPELL',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_STRONG',
                    'M2_HOSTILE',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_LORD'
            },
            'xorn': {
                'name': 'xorn',
                'symbol': 'S_XORN',
                'level': [
                    '8',
                    '9',
                    '-2',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '1200',
                    '700',
                    'MS_ROAR',
                    'MZ_MEDIUM'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_WALLWALK',
                    'M1_THICK_HIDE',
                    'M1_METALLIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'monkey': {
                'name': 'monkey',
                'symbol': 'S_YETI',
                'level': [
                    '2',
                    '12',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_SITM',
                        '0',
                        '0'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '100',
                    '50',
                    'MS_GROWL',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    '0'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'ape': {
                'name': 'ape',
                'symbol': 'S_YETI',
                'level': [
                    '4',
                    '12',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1100',
                    '500',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'owlbear': {
                'name': 'owlbear',
                'symbol': 'S_YETI',
                'level': [
                    '5',
                    '12',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_HUGS',
                        'AD_PHYS',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '1700',
                    '700',
                    'MS_ROAR',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'yeti': {
                'name': 'yeti',
                'symbol': 'S_YETI',
                'level': [
                    '5',
                    '15',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '1600',
                    '700',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    'MR_COLD'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_WHITE'
            },
            'carnivorous_ape': {
                'name': 'carnivorous ape',
                'symbol': 'S_YETI',
                'level': [
                    '6',
                    '12',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_HUGS',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '1250',
                    '550',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLACK'
            },
            'sasquatch': {
                'name': 'sasquatch',
                'symbol': 'S_YETI',
                'level': [
                    '7',
                    '15',
                    '6',
                    '0',
                    '2'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    '1550',
                    '750',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_HUMANOID',
                    'M1_SEE_INVIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'kobold_zombie': {
                'name': 'kobold zombie',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '0',
                    '6',
                    '10',
                    '0',
                    '-2'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '400',
                    '50',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'gnome_zombie': {
                'name': 'gnome zombie',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '1',
                    '6',
                    '10',
                    '0',
                    '-2'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '5'
                    )
                ],
                'size': (
                    '650',
                    '50',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_GNOME'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'orc_zombie': {
                'name': 'orc zombie',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '2',
                    '6',
                    '9',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '850',
                    '75',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_ORC'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'dwarf_zombie': {
                'name': 'dwarf zombie',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '2',
                    '6',
                    '9',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '900',
                    '150',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_DWARF'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'elf_zombie': {
                'name': 'elf zombie',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '3',
                    '6',
                    '9',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '7'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '175',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_ELF'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GREEN'
            },
            'human_zombie': {
                'name': 'human zombie',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '4',
                    '6',
                    '8',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '200',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'HI_DOMESTIC'
            },
            'ettin_zombie': {
                'name': 'ettin zombie',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '6',
                    '8',
                    '6',
                    '0',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '10'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '10'
                    )
                ],
                'size': (
                    '1700',
                    '250',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'ghoul': {
                'name': 'ghoul',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '3',
                    '6',
                    '10',
                    '0',
                    '-2'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PLYS',
                        '1',
                        '2'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '400',
                    '50',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_WANDER',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLACK'
            },
            'giant_zombie': {
                'name': 'giant zombie',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '8',
                    '8',
                    '6',
                    '0',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '2050',
                    '375',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_GIANT',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_CYAN'
            },
            'skeleton': {
                'name': 'skeleton',
                'symbol': 'S_ZOMBIE',
                'level': [
                    '12',
                    '8',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_TUCH',
                        'AD_SLOW',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '300',
                    '5',
                    'MS_BONES',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_UNDEAD',
                    'M2_WANDER',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_COLLECT',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_WHITE'
            },
            'straw_golem': {
                'name': 'straw golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '3',
                    '12',
                    '10',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '2'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '2'
                    )
                ],
                'size': (
                    '400',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_YELLOW'
            },
            'paper_golem': {
                'name': 'paper golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '3',
                    '12',
                    '10',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '400',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_PAPER'
            },
            'rope_golem': {
                'name': 'rope golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '4',
                    '9',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_HUGS',
                        'AD_PHYS',
                        '6',
                        '1'
                    )
                ],
                'size': (
                    '450',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'gold_golem': {
                'name': 'gold golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '5',
                    '9',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '3'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '3'
                    )
                ],
                'size': (
                    '450',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_ACID'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_GOLD'
            },
            'leather_golem': {
                'name': 'leather golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '6',
                    '6',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '800',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_LEATHER'
            },
            'wood_golem': {
                'name': 'wood golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '7',
                    '3',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    '900',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_NEUTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_WOOD'
            },
            'flesh_golem': {
                'name': 'flesh golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '9',
                    '8',
                    '9',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    '1',
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '1400',
                    '600',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_RED'
            },
            'clay_golem': {
                'name': 'clay golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '11',
                    '7',
                    '7',
                    '40',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '10'
                    )
                ],
                'size': (
                    '1550',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'stone_golem': {
                'name': 'stone golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '14',
                    '6',
                    '5',
                    '50',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '8'
                    )
                ],
                'size': (
                    '1900',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'glass_golem': {
                'name': 'glass golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '16',
                    '6',
                    '1',
                    '50',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '1800',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_ACID'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_CYAN'
            },
            'iron_golem': {
                'name': 'iron golem',
                'symbol': 'S_GOLEM',
                'level': [
                    '18',
                    '6',
                    '3',
                    '60',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '10'
                    ),
                    (
                        'AT_BREA',
                        'AD_DRST',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    '2000',
                    '0',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_MINDLESS',
                    'M1_HUMANOID',
                    'M1_THICK_HIDE',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'HI_METAL'
            },
            'human': {
                'name': 'human',
                'symbol': 'S_HUMAN, LVL(0, 12, 10, 0, 0), G_NOGEN, /* for corpses */\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT, M3_INFRAVISIBLE,\n         HI_DOMESTIC),\n     MON("wererat", S_HUMAN',
                'level': [
                    '2',
                    '12',
                    '10',
                    '10',
                    '-7'
                ],
                'gen_flags': (
                    '1',
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_WERE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_REGEN',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_WERE',
                    'M2_HOSTILE',
                    'M2_HUMAN',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BROWN'
            },
            'elf': {
                'name': 'elf',
                'symbol': 'S_HUMAN, LVL(10, 12, 10, 2, -3), G_NOGEN, /* for corpses */\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 8), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_ELF, 350, MS_HUMANOID, MZ_HUMAN), MR_SLEEP, MR_SLEEP,\n         M1_HUMANOID | M1_OMNIVORE | M1_SEE_INVIS,\n         M2_NOPOLY | M2_ELF | M2_STRONG | M2_COLLECT,\n         M3_INFRAVISION | M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("Woodland-elf", S_HUMAN',
                'level': [
                    '4',
                    '12',
                    '10',
                    '10',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '350',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_ELF',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GREEN'
            },
            'green-elf': {
                'name': 'Green-elf',
                'symbol': 'S_HUMAN',
                'level': [
                    '5',
                    '12',
                    '10',
                    '10',
                    '-6'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '350',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_ELF',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BRIGHT_GREEN'
            },
            'grey-elf': {
                'name': 'Grey-elf',
                'symbol': 'S_HUMAN',
                'level': [
                    '6',
                    '12',
                    '10',
                    '10',
                    '-7'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '350',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_ELF',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'elf-lord': {
                'name': 'elf-lord',
                'symbol': 'S_HUMAN',
                'level': [
                    '8',
                    '12',
                    '10',
                    '20',
                    '-9'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '350',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_ELF',
                    'M2_STRONG',
                    'M2_LORD',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BRIGHT_BLUE'
            },
            'elvenking': {
                'name': 'Elvenking',
                'symbol': 'S_HUMAN',
                'level': [
                    '9',
                    '12',
                    '10',
                    '25',
                    '-10'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '350',
                    'MS_HUMANOID',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_ELF',
                    'M2_STRONG',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'doppelganger': {
                'name': 'doppelganger',
                'symbol': 'S_HUMAN',
                'level': [
                    '9',
                    '12',
                    '5',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '12'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_IMITATE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_COLLECT',
                    'M2_SHAPESHIFTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'shopkeeper': {
                'name': 'shopkeeper',
                'symbol': 'S_HUMAN, LVL(12, 18, 0, 50, 0), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 4, 4), ATTK(AT_WEAP, AD_PHYS, 4, 4), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_SELL, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE, M2_NOPOLY | M2_HUMAN | M2_PEACEFUL\n                                        | M2_STRONG | M2_COLLECT | M2_MAGIC,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("guard", S_HUMAN, LVL(12, 12, 10, 40, 10), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 4, 10), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_GUARD, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_MERC | M2_PEACEFUL | M2_STRONG | M2_COLLECT,\n         M3_INFRAVISIBLE, CLR_BLUE),\n     MON("prisoner", S_HUMAN, LVL(12, 12, 10, 0, 0),\n         G_NOGEN, /* for special levels */\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_DJINNI, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_PEACEFUL | M2_STRONG | M2_COLLECT,\n         M3_INFRAVISIBLE | M3_CLOSE, HI_DOMESTIC),\n     MON("Oracle", S_HUMAN',
                'level': [
                    '12',
                    '0',
                    '0',
                    '50',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_NONE',
                        'AD_MAGM',
                        '0',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_ORACLE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PEACEFUL',
                    'M2_FEMALE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_ZAP'
            },
            'aligned_priest': {
                'name': 'aligned priest',
                'symbol': 'S_HUMAN, LVL(12, 12, 10, 50, 0), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 4, 10), ATTK(AT_KICK, AD_PHYS, 1, 4),\n           ATTK(AT_MAGC, AD_CLRC, 0, 0), NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_PRIEST, MZ_HUMAN), MR_ELEC, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_LORD | M2_PEACEFUL | M2_COLLECT,\n         M3_INFRAVISIBLE, CLR_WHITE),\n     /* high priests always have epri and always have ispriest set */\n     MON("high priest", S_HUMAN',
                'level': [
                    '25',
                    '15',
                    '7',
                    '70',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '10'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_CLRC',
                        '2',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_CLRC',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_PRIEST',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SEE_INVIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_MINION',
                    'M2_PRINCE',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_WHITE'
            },
            'soldier': {
                'name': 'soldier',
                'symbol': 'S_HUMAN',
                'level': [
                    '6',
                    '10',
                    '10',
                    '0',
                    '-2'
                ],
                'gen_flags': (
                    'G_SGROUP',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SOLDIER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_MERC',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'sergeant': {
                'name': 'sergeant',
                'symbol': 'S_HUMAN',
                'level': [
                    '8',
                    '10',
                    '10',
                    '5',
                    '-3'
                ],
                'gen_flags': (
                    'G_SGROUP',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SOLDIER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_MERC',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'nurse': {
                'name': 'nurse',
                'symbol': 'S_HUMAN',
                'level': [
                    '11',
                    '6',
                    '0',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '3'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_HEAL',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NURSE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'lieutenant': {
                'name': 'lieutenant',
                'symbol': 'S_HUMAN',
                'level': [
                    '10',
                    '10',
                    '10',
                    '15',
                    '-4'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SOLDIER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_MERC',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GREEN'
            },
            'captain': {
                'name': 'captain',
                'symbol': 'S_HUMAN',
                'level': [
                    '12',
                    '10',
                    '10',
                    '15',
                    '-5'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SOLDIER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_MERC',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLUE'
            },
            'watchman': {
                'name': 'watchman',
                'symbol': 'S_HUMAN',
                'level': [
                    '6',
                    '10',
                    '10',
                    '0',
                    '-2'
                ],
                'gen_flags': (
                    'G_SGROUP',
                    'G_NOGEN',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SOLDIER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_MERC',
                    'M2_STALK',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'watch_captain': {
                'name': 'watch captain',
                'symbol': 'S_HUMAN',
                'level': [
                    '10',
                    '10',
                    '10',
                    '15',
                    '-4'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SOLDIER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_MERC',
                    'M2_STALK',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GREEN'
            },
            'medusa': {
                'name': 'Medusa',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '2',
                    '50',
                    '-15'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_GAZE',
                        'AD_STON',
                        '0',
                        '0'
                    ),
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_HISS',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_PNAME',
                    'M2_FEMALE'
                ],
                'flags3': [
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BRIGHT_GREEN'
            },
            'wizard_of_yendor': {
                'name': 'Wizard of Yendor',
                'symbol': 'S_HUMAN',
                'level': [
                    '30',
                    '12',
                    '-8',
                    '100',
                    'A_NONE'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '12'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_CUSS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_SEE_INVIS',
                    'M1_TPORT',
                    'M1_TPORT_CNTRL',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_COVETOUS',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'croesus': {
                'name': 'Croesus',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '15',
                    '0',
                    '40',
                    '15'
                ],
                'gen_flags': (
                    'G_UNIQ',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '10'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_GUARD',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SEE_INVIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_PNAME',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'charon': {
                'name': 'Charon',
                'symbol': 'S_HUMAN',
                'level': [
                    '76',
                    '18',
                    '-5',
                    '120',
                    '0'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_TUCH',
                        'AD_PLYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_FERRY',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_BREATHLESS',
                    'M1_SEE_INVIS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PEACEFUL',
                    'M2_PNAME',
                    'M2_MALE',
                    'M2_GREEDY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_WHITE'
            },
            'ghost': {
                'name': 'ghost',
                'symbol': 'S_GHOST',
                'level': [
                    '10',
                    '3',
                    '-5',
                    '50',
                    '-5'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_PHYS',
                        '1',
                        '1'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '0',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_DISINT',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_WALLWALK',
                    'M1_HUMANOID',
                    'M1_UNSOLID'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_UNDEAD',
                    'M2_STALK',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'shade': {
                'name': 'shade',
                'symbol': 'S_GHOST',
                'level': [
                    '12',
                    '10',
                    '10',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_PLYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_TUCH',
                        'AD_SLOW',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '0',
                    'MS_WAIL',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_COLD',
                    'MR_DISINT',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_BREATHLESS',
                    'M1_WALLWALK',
                    'M1_HUMANOID',
                    'M1_UNSOLID',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_UNDEAD',
                    'M2_WANDER',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLACK'
            },
            'water_demon': {
                'name': 'water demon',
                'symbol': 'S_DEMON',
                'level': [
                    '8',
                    '12',
                    '-4',
                    '30',
                    '-7'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_DJINNI',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS',
                    'M1_SWIM'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BLUE'
            },
            'succubus': {
                'name': 'succubus',
                'symbol': 'S_DEMON',
                'level': [
                    '6',
                    '12',
                    '0',
                    '70',
                    '-9'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1),SEDUCTION_ATTACKS_YES,SIZ(WT_HUMAN,400,MS_SEDUCE,MZ_HUMAN),MR_FIRE',
                    'MR_POISON,0,M1_HUMANOID',
                    'M1_FLY',
                    'M1_POIS,M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_FEMALE,M3_INFRAVISIBLE',
                    'M3_INFRAVISION,CLR_GRAY),MON("horneddevil",S_DEMON,LVL(6,9,-5,50,11),(G_HELL',
                    'G_NOCORPSE',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '3'
                    ),
                    (
                        'AT_STNG',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_POIS',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BROWN'
            },
            'incubus': {
                'name': 'incubus',
                'symbol': 'S_DEMON',
                'level': [
                    '6',
                    '12',
                    '0',
                    '70',
                    '-9'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    '1),SEDUCTION_ATTACKS_YES,SIZ(WT_HUMAN,400,MS_SEDUCE,MZ_HUMAN),MR_FIRE',
                    'MR_POISON,0,M1_HUMANOID',
                    'M1_FLY',
                    'M1_POIS,M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_MALE,M3_INFRAVISIBLE',
                    'M3_INFRAVISION,CLR_GRAY),/*UsedbyAD&Dforatypeofdemon,originallyoneoftheFuriesandspelledthisway*/MON("erinys",S_DEMON,LVL(7,12,2,30,10),(G_HELL',
                    'G_NOCORPSE',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_DRST',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_FEMALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'barbed_devil': {
                'name': 'barbed devil',
                'symbol': 'S_DEMON',
                'level': [
                    '8',
                    '12',
                    '0',
                    '35',
                    '8'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_STNG',
                        'AD_PHYS',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_POIS',
                    'M1_THICK_HIDE'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'marilith': {
                'name': 'marilith',
                'symbol': 'S_DEMON',
                'level': [
                    '7',
                    '12',
                    '-6',
                    '80',
                    '-12'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_CUSS',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SLITHY',
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_FEMALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'vrock': {
                'name': 'vrock',
                'symbol': 'S_DEMON',
                'level': [
                    '8',
                    '12',
                    '0',
                    '50',
                    '-9'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'hezrou': {
                'name': 'hezrou',
                'symbol': 'S_DEMON',
                'level': [
                    '9',
                    '6',
                    '-2',
                    '55',
                    '-10'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '3'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '4',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'bone_devil': {
                'name': 'bone devil',
                'symbol': 'S_DEMON',
                'level': [
                    '9',
                    '15',
                    '-1',
                    '40',
                    '-9'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_SGROUP',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_STNG',
                        'AD_DRST',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'ice_devil': {
                'name': 'ice devil',
                'symbol': 'S_DEMON',
                'level': [
                    '11',
                    '6',
                    '-4',
                    '55',
                    '-12'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_STNG',
                        'AD_COLD',
                        '3',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_WHITE'
            },
            'nalfeshnee': {
                'name': 'nalfeshnee',
                'symbol': 'S_DEMON',
                'level': [
                    '11',
                    '9',
                    '-1',
                    '65',
                    '-11'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '4'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SPELL',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'pit_fiend': {
                'name': 'pit fiend',
                'symbol': 'S_DEMON',
                'level': [
                    '13',
                    '6',
                    '-3',
                    '65',
                    '-13'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '2'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '2'
                    ),
                    (
                        'AT_HUGS',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_GROWL',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'sandestin': {
                'name': 'sandestin',
                'symbol': 'S_DEMON',
                'level': [
                    '13',
                    '12',
                    '4',
                    '60',
                    '-5'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1500',
                    '400',
                    'MS_CUSS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_STALK',
                    'M2_STRONG',
                    'M2_COLLECT',
                    'M2_SHAPESHIFTER'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_GRAY'
            },
            'balrog': {
                'name': 'balrog',
                'symbol': 'S_DEMON',
                'level': [
                    '16',
                    '5',
                    '-2',
                    '75',
                    '-14'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '8',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_RED'
            },
            'juiblex': {
                'name': 'Juiblex',
                'symbol': 'S_DEMON',
                'level': [
                    '50',
                    '3',
                    '-7',
                    '65',
                    '-15'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_ENGL',
                        'AD_DISE',
                        '4',
                        '10'
                    ),
                    (
                        'AT_SPIT',
                        'AD_ACID',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '1500',
                    '0',
                    'MS_GURGLE',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_AMPHIBIOUS',
                    'M1_AMORPHOUS',
                    'M1_NOHEAD',
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_ACID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_NASTY',
                    'M2_LORD',
                    'M2_MALE'
                ],
                'flags3': [
                    'M3_WAITFORU',
                    'M3_WANTSAMUL',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BRIGHT_GREEN'
            },
            'yeenoghu': {
                'name': 'Yeenoghu',
                'symbol': 'S_DEMON',
                'level': [
                    '56',
                    '18',
                    '-5',
                    '80',
                    '-15'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_CONF',
                        '2',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PLYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_MAGM',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '900',
                    '500',
                    'MS_ORC',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_NASTY',
                    'M2_LORD',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_WANTSAMUL',
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'orcus': {
                'name': 'Orcus',
                'symbol': 'S_DEMON',
                'level': [
                    '66',
                    '9',
                    '-6',
                    '85',
                    '-20'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '4'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '8',
                        '6'
                    ),
                    (
                        'AT_STNG',
                        'AD_DRST',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '1500',
                    '500',
                    'MS_ORC',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_NASTY',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_WAITFORU',
                    'M3_WANTSBOOK',
                    'M3_WANTSAMUL',
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'geryon': {
                'name': 'Geryon',
                'symbol': 'S_DEMON',
                'level': [
                    '72',
                    '3',
                    '-3',
                    '75',
                    '15'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_STNG',
                        'AD_DRST',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    '1500',
                    '500',
                    'MS_BRIBE',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_POIS',
                    'M1_SLITHY'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_NASTY',
                    'M2_PRINCE',
                    'M2_MALE'
                ],
                'flags3': [
                    'M3_WANTSAMUL',
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'dispater': {
                'name': 'Dispater',
                'symbol': 'S_DEMON',
                'level': [
                    '78',
                    '15',
                    '-2',
                    '80',
                    '15'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '6',
                        '6'
                    )
                ],
                'size': (
                    '1500',
                    '500',
                    'MS_BRIBE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_POIS',
                    'M1_HUMANOID'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_NASTY',
                    'M2_PRINCE',
                    'M2_MALE',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_WANTSAMUL',
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'baalzebub': {
                'name': 'Baalzebub',
                'symbol': 'S_DEMON',
                'level': [
                    '89',
                    '9',
                    '-5',
                    '85',
                    '20'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_DRST',
                        '2',
                        '6'
                    ),
                    (
                        'AT_GAZE',
                        'AD_STUN',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1500',
                    '500',
                    'MS_BRIBE',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_NASTY',
                    'M2_PRINCE',
                    'M2_MALE'
                ],
                'flags3': [
                    'M3_WANTSAMUL',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'asmodeus': {
                'name': 'Asmodeus',
                'symbol': 'S_DEMON',
                'level': [
                    '105',
                    '12',
                    '-7',
                    '90',
                    '20'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '4',
                        '4'
                    ),
                    (
                        'AT_MAGC',
                        'AD_COLD',
                        '6',
                        '6'
                    )
                ],
                'size': (
                    '1500',
                    '500',
                    'MS_BRIBE',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_PRINCE',
                    'M2_MALE'
                ],
                'flags3': [
                    'M3_WANTSAMUL',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'demogorgon': {
                'name': 'Demogorgon',
                'symbol': 'S_DEMON',
                'level': [
                    '106',
                    '15',
                    '-8',
                    '95',
                    '-20'
                ],
                'gen_flags': (
                    'G_HELL',
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '8',
                        '6'
                    ),
                    (
                        'AT_STNG',
                        'AD_DRLI',
                        '1',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_DISE',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_DISE',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1500',
                    '500',
                    'MS_GROWL',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_NOHANDS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_NASTY',
                    'M2_PRINCE',
                    'M2_MALE'
                ],
                'flags3': [
                    'M3_WANTSAMUL',
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'HI_LORD'
            },
            'death': {
                'name': 'Death',
                'symbol': 'S_DEMON',
                'level': [
                    '30',
                    '12',
                    '-5',
                    '100',
                    '0'
                ],
                'gen_flags': (
                    'G_UNIQ',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_DETH',
                        '8',
                        '8'
                    ),
                    (
                        'AT_TUCH',
                        'AD_DETH',
                        '8',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '1',
                    'MS_RIDER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_SEE_INVIS',
                    'M1_TPORT_CNTRL'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_STRONG',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION',
                    'M3_DISPLACES'
                ],
                'color': 'HI_LORD'
            },
            'pestilence': {
                'name': 'Pestilence',
                'symbol': 'S_DEMON',
                'level': [
                    '30',
                    '12',
                    '-5',
                    '100',
                    '0'
                ],
                'gen_flags': (
                    'G_UNIQ',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_PEST',
                        '8',
                        '8'
                    ),
                    (
                        'AT_TUCH',
                        'AD_PEST',
                        '8',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '1',
                    'MS_RIDER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_SEE_INVIS',
                    'M1_TPORT_CNTRL'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_STRONG',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION',
                    'M3_DISPLACES'
                ],
                'color': 'HI_LORD'
            },
            'famine': {
                'name': 'Famine',
                'symbol': 'S_DEMON',
                'level': [
                    '30',
                    '12',
                    '-5',
                    '100',
                    '0'
                ],
                'gen_flags': (
                    'G_UNIQ',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_TUCH',
                        'AD_FAMN',
                        '8',
                        '8'
                    ),
                    (
                        'AT_TUCH',
                        'AD_FAMN',
                        '8',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '1',
                    'MS_RIDER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_HUMANOID',
                    'M1_REGEN',
                    'M1_SEE_INVIS',
                    'M1_TPORT_CNTRL'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_PNAME',
                    'M2_STRONG',
                    'M2_NASTY'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION',
                    'M3_DISPLACES'
                ],
                'color': 'HI_LORD'
            },
            'mail_daemon': {
                'name': 'mail daemon',
                'symbol': 'S_DEMON',
                'level': [
                    '56',
                    '24',
                    '10',
                    '127',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_NOCORPSE'
                ),
                'attacks': [],
                'size': (
                    '600',
                    '300',
                    'MS_SILENT',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SWIM',
                    'M1_BREATHLESS',
                    'M1_SEE_INVIS',
                    'M1_HUMANOID',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_STALK',
                    'M2_PEACEFUL'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE',
                    'M3_INFRAVISION'
                ],
                'color': 'CLR_BRIGHT_BLUE'
            },
            'djinni': {
                'name': 'djinni',
                'symbol': 'S_DEMON',
                'level': [
                    '7',
                    '12',
                    '4',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_NOCORPSE'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    '1500',
                    '400',
                    'MS_DJINNI',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_FLY',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_STALK',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_YELLOW'
            },
            'jellyfish': {
                'name': 'jellyfish',
                'symbol': 'S_EEL',
                'level': [
                    '3',
                    '3',
                    '6',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_STNG',
                        'AD_DRST',
                        '3',
                        '3'
                    )
                ],
                'size': (
                    '80',
                    '20',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_SLITHY',
                    'M1_NOLIMBS',
                    'M1_NOHEAD',
                    'M1_NOTAKE',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BLUE'
            },
            'piranha': {
                'name': 'piranha',
                'symbol': 'S_EEL',
                'level': [
                    '5',
                    '12',
                    '4',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN',
                    'G_SGROUP'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '60',
                    '30',
                    'MS_SILENT',
                    'MZ_SMALL'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_NOLIMBS',
                    'M1_CARNIVORE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_RED'
            },
            'shark': {
                'name': 'shark',
                'symbol': 'S_EEL',
                'level': [
                    '7',
                    '12',
                    '2',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '5',
                        '6'
                    )
                ],
                'size': (
                    '500',
                    '350',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_NOLIMBS',
                    'M1_CARNIVORE',
                    'M1_OVIPAROUS',
                    'M1_THICK_HIDE',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GRAY'
            },
            'giant_eel': {
                'name': 'giant eel',
                'symbol': 'S_EEL',
                'level': [
                    '5',
                    '9',
                    '-1',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '3',
                        '6'
                    ),
                    (
                        'AT_TUCH',
                        'AD_WRAP',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '200',
                    '250',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_NOLIMBS',
                    'M1_CARNIVORE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_CYAN'
            },
            'electric_eel': {
                'name': 'electric eel',
                'symbol': 'S_EEL',
                'level': [
                    '7',
                    '10',
                    '-3',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_ELEC',
                        '4',
                        '6'
                    ),
                    (
                        'AT_TUCH',
                        'AD_WRAP',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    '200',
                    '250',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_ELEC'
                ],
                'resists_conveyed': [
                    'MR_ELEC'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_ANIMAL',
                    'M1_SLITHY',
                    'M1_NOLIMBS',
                    'M1_CARNIVORE',
                    'M1_OVIPAROUS',
                    'M1_NOTAKE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BRIGHT_BLUE'
            },
            'kraken': {
                'name': 'kraken',
                'symbol': 'S_EEL',
                'level': [
                    '20',
                    '3',
                    '6',
                    '0',
                    '-3'
                ],
                'gen_flags': (
                    'G_GENO',
                    'G_NOGEN'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_HUGS',
                        'AD_WRAP',
                        '2',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '5',
                        '4'
                    )
                ],
                'size': (
                    '1800',
                    '1000',
                    'MS_SILENT',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HOSTILE',
                    'M2_STRONG'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'newt': {
                'name': 'newt',
                'symbol': 'S_LIZARD',
                'level': [
                    '0',
                    '6',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '5'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '2'
                    )
                ],
                'size': (
                    '10',
                    '20',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_YELLOW'
            },
            'gecko': {
                'name': 'gecko',
                'symbol': 'S_LIZARD',
                'level': [
                    '1',
                    '6',
                    '8',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '5'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '3'
                    )
                ],
                'size': (
                    '10',
                    '20',
                    'MS_SQEEK',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'iguana': {
                'name': 'iguana',
                'symbol': 'S_LIZARD',
                'level': [
                    '2',
                    '6',
                    '7',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '5'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '30',
                    '30',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'baby_crocodile': {
                'name': 'baby crocodile',
                'symbol': 'S_LIZARD, LVL(3, 6, 7, 0, 0), G_GENO,\n         A(ATTK(AT_BITE, AD_PHYS, 1, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(200, 200, MS_SILENT, MZ_MEDIUM), 0, 0,\n         M1_SWIM | M1_AMPHIBIOUS | M1_ANIMAL | M1_NOHANDS | M1_CARNIVORE,\n         M2_HOSTILE, 0, CLR_BROWN),\n     MON("lizard", S_LIZARD',
                'level': [
                    '5',
                    '6',
                    '6',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '5'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '10',
                    '40',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_GREEN'
            },
            'chameleon': {
                'name': 'chameleon',
                'symbol': 'S_LIZARD',
                'level': [
                    '6',
                    '5',
                    '6',
                    '10',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '2'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '4',
                        '2'
                    )
                ],
                'size': (
                    '100',
                    '100',
                    'MS_SILENT',
                    'MZ_TINY'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HOSTILE',
                    'M2_SHAPESHIFTER'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'crocodile': {
                'name': 'crocodile',
                'symbol': 'S_LIZARD',
                'level': [
                    '6',
                    '9',
                    '5',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_GENO',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '4',
                        '2'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '1',
                        '12'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_SILENT',
                    'MZ_LARGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_SWIM',
                    'M1_AMPHIBIOUS',
                    'M1_ANIMAL',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_STRONG',
                    'M2_HOSTILE'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'salamander': {
                'name': 'salamander',
                'symbol': 'S_LIZARD',
                'level': [
                    '8',
                    '12',
                    '-1',
                    '0',
                    '-9'
                ],
                'gen_flags': (
                    'G_HELL',
                    '1'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_TUCH',
                        'AD_FIRE',
                        '1',
                        '6'
                    ),
                    (
                        'AT_HUGS',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_HUGS',
                        'AD_FIRE',
                        '3',
                        '6'
                    )
                ],
                'size': (
                    '1500',
                    '400',
                    'MS_MUMBLE',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP',
                    'MR_FIRE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SLITHY',
                    'M1_THICK_HIDE',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_ORANGE'
            },
            'long_worm_tail': {
                'name': 'long worm tail',
                'symbol': 'S_WORM_TAIL',
                'level': [
                    '0',
                    '0',
                    '0',
                    '0',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_NOCORPSE',
                    'G_UNIQ'
                ),
                'attacks': [],
                'size': (
                    '0',
                    '0',
                    '0',
                    '0'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    '0L'
                ],
                'flags2': [
                    'M2_NOPOLY'
                ],
                'flags3': [
                    '0'
                ],
                'color': 'CLR_BROWN'
            },
            'archeologist': {
                'name': 'archeologist',
                'symbol': 'S_HUMAN, LVL(10, 12, 10, 1, 3), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_TUNNEL | M1_NEEDPICK | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT, M3_INFRAVISIBLE,\n         HI_DOMESTIC),\n     MON("barbarian", S_HUMAN, LVL(10, 12, 10, 1, 0), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), MR_POISON, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT, M3_INFRAVISIBLE,\n         HI_DOMESTIC),\n     MON("caveman", S_HUMAN, LVL(10, 12, 10, 0, 1), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 2, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_MALE | M2_COLLECT,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("cavewoman", S_HUMAN, LVL(10, 12, 10, 0, 1), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 2, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_FEMALE | M2_COLLECT,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("healer", S_HUMAN, LVL(10, 12, 10, 1, 0), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), MR_POISON, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT, M3_INFRAVISIBLE,\n         HI_DOMESTIC),\n     MON("knight", S_HUMAN, LVL(10, 12, 10, 1, 3), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT, M3_INFRAVISIBLE,\n         HI_DOMESTIC),\n     MON("monk", S_HUMAN, LVL(10, 12, 10, 2, 0), G_NOGEN,\n         A(ATTK(AT_CLAW, AD_PHYS, 1, 8), ATTK(AT_KICK, AD_PHYS, 1, 8), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_HERBIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT | M2_MALE,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("priest", S_HUMAN, LVL(10, 12, 10, 2, 0), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_MALE | M2_COLLECT,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("priestess", S_HUMAN, LVL(10, 12, 10, 2, 0), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_FEMALE | M2_COLLECT,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("ranger", S_HUMAN, LVL(10, 12, 10, 2, -3), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 4), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT, M3_INFRAVISIBLE,\n         HI_DOMESTIC),\n     MON("rogue", S_HUMAN, LVL(10, 12, 10, 1, -3), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_GREEDY | M2_JEWELS | M2_COLLECT,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("samurai", S_HUMAN, LVL(10, 12, 10, 1, 3), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 8), ATTK(AT_WEAP, AD_PHYS, 1, 8), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT, M3_INFRAVISIBLE,\n         HI_DOMESTIC),\n     MON("tourist", S_HUMAN, LVL(10, 12, 10, 1, 0), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT, M3_INFRAVISIBLE,\n         HI_DOMESTIC),\n     MON("valkyrie", S_HUMAN, LVL(10, 12, 10, 1, -1), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 8), ATTK(AT_WEAP, AD_PHYS, 1, 8), NO_ATTK,\n           NO_ATTK, NO_ATTK, NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), MR_COLD, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_FEMALE | M2_COLLECT,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     MON("wizard", S_HUMAN, LVL(10, 12, 10, 3, 0), G_NOGEN,\n         A(ATTK(AT_WEAP, AD_PHYS, 1, 6), NO_ATTK, NO_ATTK, NO_ATTK, NO_ATTK,\n           NO_ATTK),\n         SIZ(WT_HUMAN, 400, MS_HUMANOID, MZ_HUMAN), 0, 0,\n         M1_HUMANOID | M1_OMNIVORE,\n         M2_NOPOLY | M2_HUMAN | M2_STRONG | M2_COLLECT | M2_MAGIC,\n         M3_INFRAVISIBLE, HI_DOMESTIC),\n     /*\n      * quest leaders\n      */\n     MON("Lord Carnarvon", S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '30',
                    '20'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_TUNNEL',
                    'M1_NEEDPICK',
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'pelias': {
                'name': 'Pelias',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'shaman_karnov': {
                'name': 'Shaman Karnov',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '30',
                    '20'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'earendil': {
                'name': 'Earendil',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '50',
                    '-20'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '350',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SEE_INVIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_ELF',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISION',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'elwing': {
                'name': 'Elwing',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '50',
                    '-20'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    )
                ],
                'size': (
                    'WT_ELF',
                    '350',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_SLEEP'
                ],
                'resists_conveyed': [
                    'MR_SLEEP'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SEE_INVIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_ELF',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_FEMALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISION',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'hippocrates': {
                'name': 'Hippocrates',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '40',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'king_arthur': {
                'name': 'King Arthur',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '40',
                    '20'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'grand_master': {
                'name': 'Grand Master',
                'symbol': 'S_HUMAN',
                'level': [
                    '25',
                    '12',
                    '0',
                    '70',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '4',
                        '10'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_CLRC',
                        '2',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_CLRC',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SEE_INVIS',
                    'M1_HERBIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_NASTY',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLACK'
            },
            'arch_priest': {
                'name': 'Arch Priest',
                'symbol': 'S_HUMAN',
                'level': [
                    '25',
                    '12',
                    '7',
                    '70',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '10'
                    ),
                    (
                        'AT_KICK',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_CLRC',
                        '2',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_CLRC',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_ELEC',
                    'MR_SLEEP',
                    'MR_POISON'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_SEE_INVIS',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_WHITE'
            },
            'orion': {
                'name': 'Orion',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '30',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '2200',
                    '700',
                    'MS_LEADER',
                    'MZ_HUGE'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE',
                    'M1_SEE_INVIS',
                    'M1_SWIM',
                    'M1_AMPHIBIOUS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISION',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'master_of_thieves': {
                'name': 'Master of Thieves',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '30',
                    '-20'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'lord_sato': {
                'name': 'Lord Sato',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '30',
                    '20'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'twoflower': {
                'name': 'Twoflower',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '10',
                    '20',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_DOMESTIC'
            },
            'norn': {
                'name': 'Norn',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '80',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '8'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '1800',
                    '550',
                    'MS_LEADER',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_COLD'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_FEMALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'neferet_the_green': {
                'name': 'Neferet the Green',
                'symbol': 'S_HUMAN',
                'level': [
                    '20',
                    '12',
                    '0',
                    '60',
                    '0'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '2',
                        '8'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_LEADER',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_FEMALE',
                    'M2_PNAME',
                    'M2_PEACEFUL',
                    'M2_STRONG',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_CLOSE',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GREEN'
            },
            'minion_of_huhetotl': {
                'name': 'Minion of Huhetotl',
                'symbol': 'S_DEMON',
                'level': [
                    '16',
                    '12',
                    '-2',
                    '75',
                    '-14'
                ],
                'gen_flags': (
                    'G_NOCORPSE',
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '8',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NEMESIS',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISION',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'thoth_amon': {
                'name': 'Thoth Amon',
                'symbol': 'S_HUMAN',
                'level': [
                    '16',
                    '12',
                    '0',
                    '10',
                    '-14'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ',
                    'G_NOCORPSE'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NEMESIS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'chromatic_dragon': {
                'name': 'Chromatic Dragon',
                'symbol': 'S_DRAGON',
                'level': [
                    '16',
                    '12',
                    '0',
                    '30',
                    '-14'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_RBRE',
                        '6',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '4',
                        '8'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '4',
                        '8'
                    ),
                    (
                        'AT_STNG',
                        'AD_PHYS',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1700',
                    'MS_NEMESIS',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_DISINT',
                    'MR_ELEC',
                    'MR_POISON',
                    'MR_ACID',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_FIRE',
                    'MR_COLD',
                    'MR_SLEEP',
                    'MR_DISINT',
                    'MR_ELEC',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'flags1': [
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_CARNIVORE',
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HOSTILE',
                    'M2_FEMALE',
                    'M2_STALK',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'goblin_king': {
                'name': 'Goblin King',
                'symbol': 'S_ORC',
                'level': [
                    '15',
                    '12',
                    '10',
                    '0',
                    '-15'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '1',
                        '6'
                    )
                ],
                'size': (
                    '750',
                    '350',
                    'MS_NEMESIS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    '0'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_ORC',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_NASTY',
                    'M2_MALE',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISION',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'cyclops': {
                'name': 'Cyclops',
                'symbol': 'S_GIANT',
                'level': [
                    '18',
                    '12',
                    '0',
                    '0',
                    '-15'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '8'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '1900',
                    '700',
                    'MS_NEMESIS',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_GIANT',
                    'M2_STRONG',
                    'M2_ROCKTHROW',
                    'M2_STALK',
                    'M2_HOSTILE',
                    'M2_NASTY',
                    'M2_MALE',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISION',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_GRAY'
            },
            'ixoth': {
                'name': 'Ixoth',
                'symbol': 'S_DRAGON',
                'level': [
                    '15',
                    '12',
                    '-1',
                    '20',
                    '-14'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_BREA',
                        'AD_FIRE',
                        '8',
                        '6'
                    ),
                    (
                        'AT_BITE',
                        'AD_PHYS',
                        '4',
                        '8'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '4'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '4'
                    )
                ],
                'size': (
                    'WT_DRAGON',
                    '1600',
                    'MS_NEMESIS',
                    'MZ_GIGANTIC'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_THICK_HIDE',
                    'M1_NOHANDS',
                    'M1_CARNIVORE',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_MALE',
                    'M2_PNAME',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_STALK',
                    'M2_GREEDY',
                    'M2_JEWELS',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'master_kaen': {
                'name': 'Master Kaen',
                'symbol': 'S_HUMAN',
                'level': [
                    '25',
                    '12',
                    '-10',
                    '10',
                    '-20'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '16',
                        '2'
                    ),
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '16',
                        '2'
                    ),
                    (
                        'AT_MAGC',
                        'AD_CLRC',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NEMESIS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_HERBIVORE',
                    'M1_SEE_INVIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_MALE',
                    'M2_PNAME',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_STALK',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'nalzok': {
                'name': 'Nalzok',
                'symbol': 'S_DEMON',
                'level': [
                    '16',
                    '12',
                    '-2',
                    '85',
                    '-127'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ',
                    'G_NOCORPSE'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '8',
                        '4'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '4',
                        '6'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NEMESIS',
                    'MZ_LARGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_FLY',
                    'M1_SEE_INVIS',
                    'M1_POIS'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_DEMON',
                    'M2_MALE',
                    'M2_PNAME',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_NASTY',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISION',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_RED'
            },
            'scorpius': {
                'name': 'Scorpius',
                'symbol': 'S_SPIDER',
                'level': [
                    '15',
                    '12',
                    '10',
                    '0',
                    '-15'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_CLAW',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '6'
                    ),
                    (
                        'AT_STNG',
                        'AD_DISE',
                        '1',
                        '4'
                    )
                ],
                'size': (
                    '750',
                    '350',
                    'MS_NEMESIS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_POISON',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_POISON'
                ],
                'flags1': [
                    'M1_ANIMAL',
                    'M1_NOHANDS',
                    'M1_OVIPAROUS',
                    'M1_POIS',
                    'M1_CARNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_MALE',
                    'M2_PNAME',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU'
                ],
                'color': 'HI_LORD'
            },
            'master_assassin': {
                'name': 'Master Assassin',
                'symbol': 'S_HUMAN',
                'level': [
                    '15',
                    '12',
                    '0',
                    '30',
                    '18'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_DRST',
                        '2',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '8'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NEMESIS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_STRONG',
                    'M2_MALE',
                    'M2_HOSTILE',
                    'M2_STALK',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'ashikaga_takauji': {
                'name': 'Ashikaga Takauji',
                'symbol': 'S_HUMAN',
                'level': [
                    '15',
                    '12',
                    '0',
                    '40',
                    '-13'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ',
                    'G_NOCORPSE'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NEMESIS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_PNAME',
                    'M2_HOSTILE',
                    'M2_STRONG',
                    'M2_STALK',
                    'M2_NASTY',
                    'M2_MALE',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'lord_surtur': {
                'name': 'Lord Surtur',
                'symbol': 'S_GIANT',
                'level': [
                    '15',
                    '12',
                    '2',
                    '50',
                    '12'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '10'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '2',
                        '10'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '2',
                        '6'
                    )
                ],
                'size': (
                    '2250',
                    '850',
                    'MS_NEMESIS',
                    'MZ_HUGE'
                ),
                'resists': [
                    'MR_FIRE',
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    'MR_FIRE'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_GIANT',
                    'M2_MALE',
                    'M2_PNAME',
                    'M2_HOSTILE',
                    'M2_STALK',
                    'M2_STRONG',
                    'M2_NASTY',
                    'M2_ROCKTHROW',
                    'M2_JEWELS',
                    'M2_COLLECT'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISION',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'HI_LORD'
            },
            'dark_one': {
                'name': 'Dark One',
                'symbol': 'S_HUMAN',
                'level': [
                    '15',
                    '12',
                    '0',
                    '80',
                    '-10'
                ],
                'gen_flags': (
                    'G_NOGEN',
                    'G_UNIQ',
                    'G_NOCORPSE'
                ),
                'attacks': [
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_WEAP',
                        'AD_PHYS',
                        '1',
                        '6'
                    ),
                    (
                        'AT_CLAW',
                        'AD_SAMU',
                        '1',
                        '4'
                    ),
                    (
                        'AT_MAGC',
                        'AD_SPEL',
                        '0',
                        '0'
                    )
                ],
                'size': (
                    'WT_HUMAN',
                    '400',
                    'MS_NEMESIS',
                    'MZ_HUMAN'
                ),
                'resists': [
                    'MR_STONE'
                ],
                'resists_conveyed': [
                    '0'
                ],
                'flags1': [
                    'M1_HUMANOID',
                    'M1_OMNIVORE'
                ],
                'flags2': [
                    'M2_NOPOLY',
                    'M2_HUMAN',
                    'M2_STRONG',
                    'M2_HOSTILE',
                    'M2_STALK',
                    'M2_NASTY',
                    'M2_COLLECT',
                    'M2_MAGIC'
                ],
                'flags3': [
                    'M3_WANTSARTI',
                    'M3_WAITFORU',
                    'M3_INFRAVISIBLE'
                ],
                'color': 'CLR_BLACK'
            }
        }    
        }
    }