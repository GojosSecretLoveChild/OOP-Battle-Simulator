import random

class Hero:

    global crit
    crit = "Critical Hit!"
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 10

    def critical_hit(self):
        crit_chance = random.randint(1, 100)
        if crit_chance <= 20:
            print(crit)
            return random.randint(5, 20)
        return 0

    def attack(self, target):
        damage = self.attack_power + self.critical_hit()
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
