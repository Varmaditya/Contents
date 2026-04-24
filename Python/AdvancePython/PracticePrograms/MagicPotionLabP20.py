# Program: Magic Potion Lab

class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self):
        print(f"You used {self.name}! Effect:", self.effect)


class PotionLab:
    def __init__(self):
        self.potions = []

    def create_potion(self):
        name = input("Potion name: ")
        effect = input("Effect: ")
        potion = Potion(name, effect)
        self.potions.append(potion)
        print("Potion created!")

    def use_potion(self):
        for i, p in enumerate(self.potions, 1):
            print(i, p.name)

        choice = int(input("Choose potion: "))
        self.potions[choice - 1].use()


lab = PotionLab()

while True:
    print("\n=== Potion Lab ===")
    print("1. Create Potion")
    print("2. Use Potion")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        lab.create_potion()
    elif choice == "2":
        lab.use_potion()
    elif choice == "3":
        break