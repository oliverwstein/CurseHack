from monster_data import MonsterData

class Attack:
    def __init__(self, attack_type, damage_type, num_dice, num_sides):
        self.attack_type = attack_type  # Type of attack (e.g., bite, claw)
        self.damage_type = damage_type  # Type of damage (e.g., physical, fire)
        self.num_dice = num_dice        # Number of dice to roll for damage
        self.num_sides = num_sides      # Number of sides on each die

class Monster:
    def __init__(self, name):
        if name not in MonsterData.monsters:
            raise ValueError(f"Unknown monster name: {name}")

        monster_data = MonsterData.monsters[name]

        self.name = name
        self.symbol = monster_data["symbol"]
        self.level, self.move_rate, self.armor_class, self.magic_resistance, self.alignment = monster_data["level"]
        self.generation_flags = monster_data["gen_flags"]
        self.attacks = [Attack(*atk) for atk in monster_data["attacks"]]
        self.weight, self.nutritional_value, self.sound, self.size = monster_data["size"]
        self.mr1 = monster_data["mr1"]
        self.mr2 = monster_data["mr2"]
        self.flags1 = monster_data["flags1"]
        self.flags2 = monster_data["flags2"]
        self.flags3 = monster_data["flags3"]
        self.color = monster_data["color"]