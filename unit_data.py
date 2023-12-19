class UnitData:
    classes = {
        "Wizard": {'base_stats':
                        {'str': 7,
                        'dex': 7,
                        'con': 7,
                        'int': 10,
                        'wis': 7,
                        'cha': 7,
                        },
                    'growths':
                        {'str': 10,
                        'dex': 20,
                        'con': 20,
                        'int': 30,
                        'wis': 10,
                        'cha': 10
                        },
                    'hp':
                        {'starting': 10},
                    },
    }
    races = {
        "Human": { 
            'max_stats': {
                'str': 18,
                'dex': 18,
                'con': 18,
                'int': 18,
                'wis': 18,
                'cha': 18
            },
            'hp':
                {'starting': 2},
            
        },
        "Elf": {
            'max_stats': {
                'str': 18,
                'dex': 18,
                'con': 16,
                'int': 20,
                'wis': 20,
                'cha': 18
            },
            'hp':
                {'starting': 1},
        },
        "Dwarf": {
            'max_stats': {
                'str': 18,
                'dex': 20,
                'con': 20,
                'int': 16,
                'wis': 16,
                'cha': 16
            },
            'hp':
                {'starting': 4},
        },
        "Gnome": {
            'max_stats': {
                'str': 18,
                'dex': 18,
                'con': 18,
                'int': 19,
                'wis': 18,
                'cha': 18
            },
            'hp':
                {'starting': 1},
        },
        "Orc": {
            'max_stats': {
                'str': 18,
                'dex': 18,
                'con': 18,
                'int': 16,
                'wis': 16,
                'cha': 16
            },
            'hp':
                {'starting': 1},
        }
    }