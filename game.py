from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Lung"


def main():
    print(f"Welcome to {ARENA_NAME}!")
    print("The oceans are opening...")

    hero = Hero("Markiplier")

    goblin1 = Goblin("Gribble")
    goblin2 = Goblin("Sribble")

    print(f"{goblin1.name} enters the water with {goblin1.health} health.")
    print(f"{goblin2.name} enters the water with {goblin2.health} health.")
    print(f"The hero, {hero.name} enters the water with {hero.health} health.")

    hero.attack(goblin1)
    if goblin1.is_alive():
        goblin1.attack(hero)

if __name__ == "__main__":
    main()
