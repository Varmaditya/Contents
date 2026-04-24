# Program: Virtual Pet Game

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5

    def eat(self):
        self.hunger = max(0, self.hunger - 2)
        print(self.name, "is eating.")

    def play(self):
        self.energy -= 2
        self.hunger += 1
        print(self.name, "is playing!")

    def status(self):
        print(f"{self.name} -> Hunger: {self.hunger}, Energy: {self.energy}")


pet_name = input("Name your pet: ")
pet = Pet(pet_name)

while True:
    print("\n=== Pet Menu ===")
    print("1. Feed")
    print("2. Play")
    print("3. Check Status")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pet.eat()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.status()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")