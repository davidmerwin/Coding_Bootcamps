"""
Guess the Number Game. This program generates a random number between two given bounds and prompts the
user to guess the number. Provides feedback on each guess until the user guesses the correct number.
Usage: python guess_number.py
"""

from random import randint
import sys

# Parse command line arguments for min and max bounds
min_bound: int = int(sys.argv[1])
max_bound: int = int(sys.argv[2])

# Generate random number between min and max bounds
answer: int = randint(min_bound, max_bound)


def get_guess() -> int:
    """
    Prompts user for a number guess and returns the guess as an integer.
    Validates that the input is a number between min and max bounds.
    """

    while True:
        try:
            guess: int = int(input(f'Guess a number between {min_bound} and {max_bound}: '))

            if min_bound < guess < max_bound:
                return guess
            else:
                print(f'Please enter a number between {min_bound} and {max_bound}')

        except ValueError:
            print('Please enter a valid number')


def check_guess(guess: int) -> None:
    """
    Checks if the guess matches the answer.
    Prints a message whether the guess is correct or incorrect.
    """

    if guess == answer:
        print('You are a genius!!!!!')
    else:
        print('Incorrect guess...........')


def play_game() -> None:
    """
    Runs the guess the number game loop, calling functions
    to prompt for guesses and check if guess is correct.
    Ends when correct guess is made.
    """

    while True:
        guess = get_guess()
        check_guess(guess)

        if guess == answer:
            break


# run the guess game
if __name__ == '__main__':
    play_game()








