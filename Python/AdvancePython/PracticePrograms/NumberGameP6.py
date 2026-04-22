# Program: Number Guessing Game (with difficulty levels)

import random

def play_game(max_number, attempts):
    number = random.randint(1, max_number)

    print(f"\nGuess the number between 1 and {max_number}")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("Correct! You guessed it!")
            return

        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        print("Attempts left:", attempts)

    print("You lost! The number was:", number)


while True:
    print("\n=== Number Guessing Game ===")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")
    print("4. Exit")

    choice = input("Choose difficulty: ")

    if choice == "1":
        play_game(10, 5)
    elif choice == "2":
        play_game(50, 7)
    elif choice == "3":
        play_game(100, 10)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")