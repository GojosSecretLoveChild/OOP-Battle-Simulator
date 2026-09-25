import random
from goblin import Goblin
from hero import Hero
from boss import Brute

def main():
    print("Welcome to the Iron Lung!")

    hero = Hero("Markiplier")

    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]

    defeated_goblins = 0

    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins!")
    else:
        print(f"\nThe hero has been defeated. Game Over.")

    if hero.is_alive():
        print("BOSS TIME!!!")
        brutus = Brute("Brutus")
        while hero.is_alive() and brutus.is_alive():
            damage = hero.strike()
            brutus.take_damage(damage)
            damage = brutus.attack()
            hero.receive_damage(damage)
    
    if hero.is_alive():
        print(f"\nThe hero has defeated the BOSS!")
    else:
        print(f"\nThe BOSS beat the Hero. Game Over.")

    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()