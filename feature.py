from feature_data import FeatureData
class Feature:
    def __init__(self, x, y, feat):
        if feat not in FeatureData.features:
            raise ValueError(f"Unknown feature: {feat}")
        self._x = x
        self._y = y
        self.attrs = FeatureData.features[feat]

    @property
    def pos(self):
        return (self._x, self._y)

    @pos.setter
    def pos(self, xy):
        if not isinstance(xy, tuple) or len(xy) != 2:
            raise ValueError("Position must be a tuple of two elements: (x, y)")
        self._x, self._y = xy

    # Example of usage
    # To get the position
    # feature_instance.pos

    # To set the position
    # feature_instance.pos = (new_x, new_y)
