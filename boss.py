from enemy import Enemy

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, health=50, attack_power=15)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} unleashes a swift blow!")
        return damage + bonus_damage