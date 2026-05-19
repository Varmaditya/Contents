# Program: Ultimate Battle Arena ⚔️🔥

import random
import time


def battle_log(func):

    # Decorator for battle logs

    def wrapper(*args, **kwargs):

        print("\n" + "=" * 50)
        print("⚔️  BATTLE ROUND STARTED ⚔️")
        print("=" * 50)

        result = func(*args, **kwargs)

        print("=" * 50)
        print("🏁 ROUND ENDED")
        print("=" * 50 + "\n")

        return result

    return wrapper


class Player:

    def __init__(self, name):

        self.name = name
        self.health = 100
        self.max_health = 100

        # Inventory items
        self.inventory = {
            "Potion": 2,
            "Mega Potion": 1
        }

        # Attack types
        self.attacks = {
            "Slash ⚔️": (10, 20),
            "Fireball 🔥": (15, 30),
            "Thunder Strike ⚡": (5, 35),
            "Poison Attack ☠️": (8, 18)
        }

    def show_status(self):

        print("\n🧍", self.name)
        print("❤️ Health:", self.health)

        print("🎒 Inventory:")

        for item, qty in self.inventory.items():
            print(f"   {item} -> {qty}")

    def attack(self):

        print("\nChoose Attack:")

        attack_list = list(self.attacks.keys())

        for i, atk in enumerate(attack_list, 1):
            print(f"{i}. {atk}")

        try:

            choice = int(input("Enter attack choice: "))

            if choice < 1 or choice > len(attack_list):
                raise ValueError

            selected_attack = attack_list[choice - 1]

            min_dmg, max_dmg = self.attacks[selected_attack]

            damage = random.randint(min_dmg, max_dmg)

            print(
                f"\n💥 {self.name} used {selected_attack}"
            )

            print(f"🔥 Damage Dealt: {damage}")

            return damage

        except ValueError:

            print("❌ Invalid attack! Turn wasted.")

            return 0

    def heal(self):

        print("\nChoose Healing Item:")
        print("1. Potion (+20 HP)")
        print("2. Mega Potion (+40 HP)")

        choice = input("Choice: ")

        if choice == "1":

            if self.inventory["Potion"] > 0:

                self.health += 20

                if self.health > self.max_health:
                    self.health = self.max_health

                self.inventory["Potion"] -= 1

                print(f"🧪 {self.name} used Potion!")
                print("❤️ +20 Health Restored!")

            else:
                print("❌ No Potion left!")

        elif choice == "2":

            if self.inventory["Mega Potion"] > 0:

                self.health += 40

                if self.health > self.max_health:
                    self.health = self.max_health

                self.inventory["Mega Potion"] -= 1

                print(f"✨ {self.name} used Mega Potion!")
                print("❤️ +40 Health Restored!")

            else:
                print("❌ No Mega Potion left!")

        else:
            print("❌ Invalid healing choice!")

    def alive(self):

        return self.health > 0


class Arena:

    def __init__(self, p1, p2):

        self.p1 = p1
        self.p2 = p2

    def turns(self):

        # Generator for turn switching

        while True:

            yield self.p1
            yield self.p2

    @battle_log
    def start(self):

        print("\n🎮 WELCOME TO ULTIMATE BATTLE ARENA 🎮")

        turn_generator = self.turns()

        round_no = 1

        while self.p1.alive() and self.p2.alive():

            print(f"\n🌀 ROUND {round_no}")

            current = next(turn_generator)

            enemy = self.p2 if current == self.p1 else self.p1

            current.show_status()

            print("\nChoose Action:")
            print("1. Attack ⚔️")
            print("2. Heal 🧪")

            action = input("Enter choice: ")

            if action == "1":

                damage = current.attack()

                enemy.health -= damage

                if enemy.health < 0:
                    enemy.health = 0

                print(
                    f"\n💀 {enemy.name} now has {enemy.health} HP"
                )

            elif action == "2":

                current.heal()

            else:
                print("❌ Invalid action!")

            time.sleep(1)

            round_no += 1

        winner = self.p1 if self.p1.alive() else self.p2

        print("\n" + "🏆" * 10)
        print(f"🏆 WINNER IS {winner.name.upper()} 🏆")
        print("🏆" * 10)


# ---------------- MAIN GAME ----------------

print("🔥 Welcome Warriors! 🔥")

p1_name = input("Enter Player 1 Name: ")
p2_name = input("Enter Player 2 Name: ")

p1 = Player(p1_name)
p2 = Player(p2_name)

arena = Arena(p1, p2)

arena.start()
