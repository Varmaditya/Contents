# Program: Infinite Loot Generator

import random

class LootBox:
    def __init__(self):
        self.items = ["Gold", "Sword", "Shield", "Potion", "Gem"]

    def generate_loot(self):
        # Generator that yields items infinitely
        while True:
            yield random.choice(self.items)


loot_box = LootBox()
loot_stream = loot_box.generate_loot()

for _ in range(5):
    input("\nOpen loot box...")
    print("You got:", next(loot_stream))