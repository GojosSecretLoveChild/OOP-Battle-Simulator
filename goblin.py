import random
from hero import crit


class Goblin:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        if crit == True:
            print(crit)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
