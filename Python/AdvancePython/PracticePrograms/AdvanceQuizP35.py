# Program: Advanced Quiz System

import random


class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def ask(self):
        print("\n" + self.text)

        # Display options
        for i, opt in enumerate(self.options, 1):
            print(f"{i}. {opt}")

        try:
            choice = int(input("Enter option number: "))

            if choice < 1 or choice > len(self.options):
                raise ValueError("Choice out of range!")

            selected = self.options[choice - 1]

            if selected.lower() == self.answer.lower():
                print("Correct!")
                return 1
            else:
                print("Wrong! Correct answer:", self.answer)
                return 0

        except ValueError as ve:
            print("Invalid input!", ve)
            return 0


class QuizGame:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []

    def load_questions(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split("|")

                    # Format: question|opt1,opt2,opt3|answer
                    text = parts[0]
                    options = parts[1].split(",")
                    answer = parts[2]

                    self.questions.append(Question(text, options, answer))

        except FileNotFoundError:
            print("Question file not found!")

    def play(self):
        if not self.questions:
            print("No questions loaded!")
            return

        score = 0

        random.shuffle(self.questions)

        for q in self.questions:
            score += q.ask()

        print("\nFinal Score:", score, "/", len(self.questions))

        name = input("Enter your name: ")

        # Save score
        try:
            with open("quiz_scores.txt", "a") as file:
                file.write(f"{name}:{score}/{len(self.questions)}\n")
        except Exception as e:
            print("Error saving score:", e)

    def show_scores(self):
        try:
            with open("quiz_scores.txt", "r") as file:
                print("\n=== Leaderboard ===")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No scores yet!")


# ---------------- Main Program ----------------

quiz = QuizGame("questions.txt")
quiz.load_questions()

while True:
    print("\n=== Advanced Quiz System ===")
    print("1. Play Quiz")
    print("2. Show Leaderboard")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        quiz.play()

    elif choice == "2":
        quiz.show_scores()

    elif choice == "3":
        break

    else:
        print("Invalid choice!")


# Make a file with quiz question like given below:
# Capital of France?|Paris,London,Berlin|Paris
# 5 + 7?|10,11,12|12
# Color of sky?|Blue,Green,Red|Blue
# Largest planet?|Earth,Mars,Jupiter|Jupiter