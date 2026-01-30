# Program: Word guessing game

import random

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
secretWord = random.choice(words)
clue = list('?????')
heartSymbol = u'\u2764'
guessedWordCorrectly = False
unknownLetters = len(secretWord)

def update_clue(guessedLetter, secretWord, clue, unknownLetters):
    index = 0

    while index < len(secretWord):
        if guessedLetter == secretWord[index]:
            clue[index] = guessedLetter
            unknownLetters = unknownLetters - 1
        index = index + 1

    return unknownLetters

while lives > 0:
    print(clue)
    print("Lives left: " + heartSymbol * lives)
    guess = input("Guess a letter or the whole word: ")

    if guess == secretWord:
        guessedWordCorrectly = True
        break

    if guess in secretWord:
        unknownLetters = update_clue(guess, secretWord, clue, unknownLetters)
    else:
        print("Incorrect. You lose a life!")
        lives = lives - 1

    if unknownLetters == 0:
        guessedWordCorrectly = True
        break

if guessedWordCorrectly:
    print("You won! The secret word was: " + secretWord)
else:
    print("You lost! The secret word was: " + secretWord)