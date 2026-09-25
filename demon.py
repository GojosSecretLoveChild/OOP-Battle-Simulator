import random
from enemy import Enemy

class Demon(Enemy):

    def __init__(self, name):
        super().__init__(name, 100, 10)
