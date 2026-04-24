# Program: Zombie Survival Game

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self):
        return random.randint(10, 25)

    def take_damage(self, dmg):
        self.health -= dmg
        print(self.name, "took", dmg, "damage! Health:", self.health)


class Zombie:
    def attack(self):
        return random.randint(5, 20)


player = Player(input("Enter your name: "))
zombie = Zombie()

while player.health > 0:
    print("\nA zombie appears!")

    action = input("Attack or Run? ").lower()

    if action == "attack":
        damage = player.attack()
        print("You hit zombie for", damage)

        zombie_damage = zombie.attack()
        player.take_damage(zombie_damage)

    elif action == "run":
        print("You escaped!")
        break

    else:
        print("Invalid action!")

if player.health <= 0:
    print("You were eaten by zombies!")