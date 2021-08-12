"""Write a guessing game where the user has to guess a secret number. After every guess the program
tells the user whether their number was too large or too small. At the end the number of tries needed
should be printed. It counts only as one try if they input the same number multiple times consecutively."""

import numpy as np

x = int(input("Welcome to the guessing game, choose a number: "))
print(x)
secretNumber = np.random.randint(1, 100)
guesses = []
while x != secretNumber:
    if x > secretNumber:
        x = int(input("Too large guess, try again: "))
        if x not in guesses: guesses.append(x)
    elif x < secretNumber:
        x = int(input("Too small guess, try again: "))
        if x not in guesses: guesses.append(x)
print("You won after",len(guesses),"guesses !")