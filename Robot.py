from weapon import Weapon

class Robot:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level
        self.health = 1000
        self.weapon = Weapon('laser', 50)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power