# Program: Password Generator

import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red',
              'orange', 'yellow', 'green','blue', 'purple', 'fluffy',
              'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda']

print("Welcome to Password Picker!")

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    specialChar = random.choice(string.punctuation)

    password = adjective + noun + str(number) + specialChar
    print("Your new password is: ", password)

    response = input("Would you like another password? (y/n): ")
    if response == "n":
        break