# Write a function guessing_game that takes no argument
# The function:
    # Chooses a random integer between 0 and 100 inclusive
    # Asks the user to guess what number has been chosen
    # Each time the user enters a guess, the program outputs:
        # Too high
        # Too low
        # Just right
    # If the user guesses correctly, the program exits.
    # Otherwise, the user is asked to try again.
    # The program only exits after the user guesses correctly
import random

def guessing_game():
    number = random.randint(0,100)
    while True:
        guess = int(input("Please guess a number from 0 to 100 inclusive: "))
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else: 
            print("Just right")
            break
guessing_game()
