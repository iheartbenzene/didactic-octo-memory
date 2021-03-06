import random

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    def defense_roll(self):
        roll = random.randint(1, 6)
        return roll * self.level
    
class Dragon(Creature):
    def __init__(self, name, level, armor, breath):
        super().__init__(name, level)
        self.armor = armor
        self.breath = breath
        
    def defense_roll(self):
        roll = super().defense_roll()
        value = roll * self.armor
        if self.breath:
            value = value * 2
        return value

class Wizard(Creature):
    
    def attack_roll(self, creature):
        my_roll = self.defense_roll()
        creature_roll = creature.defense_roll
    
        return my_roll >= creature_roll
    