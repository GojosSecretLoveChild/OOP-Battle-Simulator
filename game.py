import random
from demon import Demon
from hero import Hero
from boss import Boss

def main():
    print("Welcome To The Iron Lung.")
    hero = Hero("Markiplier")

    demons = [Demon(f"Demon {i+1}") for i in range(2)]
    defeated_demons = 0

    while hero.is_alive() and any(demon.is_alive() for demon in demons):
        print("You Venture Futher Into The Depths...")
        
        target_demon = random.choice([demon for demon in demons if demon.is_alive()])
        damage = hero.strike()
        print(f"Markiplier Blocks Out {target_demon.name} For {damage} Focus.")
        target_demon.take_damage(damage)

        if not target_demon.is_alive():
            defeated_demons += 1
            print(f"{target_demon.name} Has Been Warded... For Now.")

        for demon in demons:
            if demon.is_alive():
                damage = demon.attack()
                print(f"{demon.name} Attacks The Iron Lung For {damage} Force.")
                hero.receive_damage(damage)

    if hero.is_alive():
        print(f"All The Demons Have Been Wardered.")
    else:
        print(f"You Have Been Consumed By The Ocean Of Blood.")

    if hero.is_alive():
        angler = Boss("The Angler")
        while hero.is_alive() and angler.is_alive():
            damage = hero.strike()
            angler.take_damage(damage)
            damage = angler.attack()
            hero.receive_damage(damage)
    
    if hero.is_alive():
        print(f"The Ship Is Saved At Last...")
    else:
        print(f"You Have Been Consumed By The Ocean Of Blood.")

    print(f"Total Demons Warded: {defeated_demons} / {len(demons)}.")

if __name__ == "__main__":
    main()