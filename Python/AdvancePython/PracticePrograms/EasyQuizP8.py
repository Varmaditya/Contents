# Program: General Knowledge Quiz

questions = [
    ("Capital of India?", "delhi"),
    ("5 + 7 = ?", "12"),
    ("Color of sky?", "blue")
]

def run_quiz():
    score = 0

    for question, answer in questions:
        user = input(question + " ")

        if user.lower() == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Answer:", answer)

    print("Final Score:", score)


while True:
    print("\n=== Quiz Game ===")
    print("1. Start Quiz")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        run_quiz()
    elif choice == "2":
        break
    else:
        print("Invalid choice!")