# Program: High Score Tracker

class ScoreBoard:
    def __init__(self, filename):
        self.filename = filename

    def add_score(self):
        name = input("Enter player name: ")
        score = input("Enter score: ")

        with open(self.filename, "a") as file:
            file.write(f"{name},{score}\n")

        print("Score saved!")

    def show_scores(self):
        try:
            with open(self.filename, "r") as file:
                print("\nHigh Scores:")
                for line in file:
                    name, score = line.strip().split(",")
                    print(name, "->", score)
        except FileNotFoundError:
            print("No scores yet!")


board = ScoreBoard("scores.txt")

while True:
    print("\n=== Score Board ===")
    print("1. Add Score")
    print("2. View Scores")
    print("3. Exit")

    if input("Choice: ") == "1":
        board.add_score()
    elif input("Choice again (2/3): ") == "2":
        board.show_scores()
    else:
        break