# Program: Advanced Quiz Game

import random

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def ask(self):
        print("\n" + self.text)

        for i, opt in enumerate(self.options, 1):
            print(f"{i}. {opt}")

        choice = input("Enter option number: ")

        if self.options[int(choice) - 1].lower() == self.answer.lower():
            print("Correct!")
            return True
        else:
            print("Wrong! Correct answer:", self.answer)
            return False


def run_quiz(questions):
    score = 0

    random.shuffle(questions)

    for q in questions:
        if q.ask():
            score += 1

    return score


easy_questions = [
    Question("Capital of India?", ["Delhi", "Mumbai", "Chennai"], "Delhi"),
    Question("2 + 2?", ["3", "4", "5"], "4")
]

hard_questions = [
    Question("Square root of 144?", ["10", "12", "14"], "12"),
    Question("Python is a?", ["Snake", "Language", "Game"], "Language")
]


while True:
    print("\n=== Quiz Game ===")
    print("1. Easy Level")
    print("2. Hard Level")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        score = run_quiz(easy_questions)

    elif choice == "2":
        score = run_quiz(hard_questions)

    elif choice == "3":
        break

    else:
        print("Invalid choice!")
        continue

    print("\nYour Score:", score)

    if score == 2:
        print("Excellent!")
    elif score == 1:
        print("Good job!")
    else:
        print("Better luck next time!")