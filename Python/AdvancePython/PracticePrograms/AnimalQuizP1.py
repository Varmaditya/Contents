def check_guess(guess, answer):
    global score
    stillGuessing = True
    attempt = 0

    while stillGuessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer!")
            score += 1
            stillGuessing = False
        else:
            if attempt < 2:
                guess = input("Wrong answer. Try again! ")
            attempt += 1

    if attempt == 3:
        print("The correct answer is " + answer)

score = 0
print("Guess the Animal")

guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")

guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "cheetah")

guess3 = input("Which is the largest animal? ")
check_guess(guess3, "blue whale")

print("Your score is " + str(score))