import random
from feature_data import FeatureData
from tile import *

class Feature:
    def __init__(self, x, y, feat=None):
        if feat is None:
            feat = self.random_feature_based_on_rarity()

        if feat not in FeatureData.features:
            raise ValueError(f"Unknown feature: {feat}")

        self._x = x
        self._y = y

        # Generate a single tile based on the feature data
        self.feature_info = FeatureData.features[feat]
        self.tile = self.generate_tile(x, y)

    @staticmethod
    def random_feature_based_on_rarity():
        # Filter out features not meant for random generation
        filtered_features = {feat: attrs for feat, attrs in FeatureData.features.items() if attrs.get('random', True)}

        # Group features by rarity
        rarity_groups = {}
        for feat, attrs in filtered_features.items():
            rarity = attrs['rarity']
            rarity_groups.setdefault(rarity, []).append(feat)

        # Calculate weights for each rarity group and normalize within the group
        normalized_weights = {}
        for rarity, feats in rarity_groups.items():
            group_weight = 1 / (2 ** rarity)
            weight_per_feature = group_weight / len(feats)
            for feat in feats:
                normalized_weights[feat] = weight_per_feature

        # Weighted random selection based on the normalized weights
        total_weight = sum(normalized_weights.values())
        random_choice = random.uniform(0, total_weight)
        cumulative_weight = 0
        for feature, weight in normalized_weights.items():
            cumulative_weight += weight
            if random_choice <= cumulative_weight:
                return feature


    def generate_tile(self, x, y):
        # Instantiate the correct Tile subclass based on feature data
        if self.feature_info['tile'] == Water:
            return Water(x, y, self.feature_info.get('depth', 'shallow'), self.feature_info.get('state', 'pool'))
        elif self.feature_info['tile'] == Spring:
            return Spring(x, y, self.feature_info.get('depth', 'Deep'), self.feature_info.get('state', 'hot'))
        elif self.feature_info['tile'] == Veg:
            return Veg(x, y, self.feature_info.get('variant', 'moss'))
        elif self.feature_info['tile'] == Rock:
            return Rock(x, y, self.feature_info.get('state', 'solid'))
        # Add other cases for different tile types if needed


    @property
    def pos(self):
        return (self._x, self._y)

    @pos.setter
    def pos(self, xy):
        if not isinstance(xy, tuple) or len(xy) != 2:
            raise ValueError("Position must be a tuple of two elements: (x, y)")
        self._x, self._y = xy
        # Update the position of the tile
        self.tile.pos = xy
