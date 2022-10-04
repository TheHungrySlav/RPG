class Magic:
    def __init__(self,mana_cost,type,damage):
        self.mana_cost = mana_cost
        self.type = type
        self.damage = damage

# Magic List
# Basic spells
fireball = Magic(5,'fire',10)
blade_of_wind = Magic(5,'wind',10)
wild_water_wave = Magic(5,'water',10)
lightning_strike = Magic(5,'lightning',10)
tearing_earth = Magic(5,'stone',10)

