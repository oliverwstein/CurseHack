from tile import *
class FeatureData:
    features = {
        'door': {
            'tile': Door,
            'state': 'closed',
            'color': 'black',
            'random': False,
        },
        'stair': {
            'tile': Stair,
            'state': 'up',
            'color': 'black',
            'random': False,
        },
        'stair': {
            'tile': Stair,
            'state': 'down',
            'color': 'black',
            'random': False,
        },
        'floor': {
            'tile': Floor,
            'color': 'black',
            'random': False,
        },
        'wall': {
            'tile': Wall,
            'color': 'black',
            'random': False,
        },
        'spring': {
            'tile': Water,
            'depth': 'shallow',
            'state': 'fresh',
            'color': 'blue',
            'random': True,
            'rarity': 3,
        },
        'hot_spring': {
            'tile': Water,
            'depth': 'shallow',
            'state': 'sulfurous',
            'color': 'cyan',
            'random': True,
            'rarity': 3,
        },
        'pool': {
            'tile': Water,
            'depth': 'shallow',
            'state': 'fresh',
            'color': 'blue',
            'random': True,
            'rarity': 2,
        },
        'stag_pool': {
            'tile': Water,
            'depth': 'shallow',
            'state': 'stagnant',
            'color': 'blue',
            'random': True,
            'rarity': 2,
        },
        'rock': {
            'tile': Rock,
            'color': 'gray',
            'random': True,
            'rarity': 1,
        },

    }
