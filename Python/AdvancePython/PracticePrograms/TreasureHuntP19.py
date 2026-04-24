# Program: Treasure Hunt Game

import random

class Player:
    def __init__(self):
        self.score = 0

    def find_treasure(self):
        found = random.choice([True, False])

        if found:
            self.score += 10
            print("You found treasure! +10 points")
        else:
            print("Nothing here...")


player = Player()

for i in range(5):
    input("\nPress Enter to search...")
    player.find_treasure()

print("Final Score:", player.score)