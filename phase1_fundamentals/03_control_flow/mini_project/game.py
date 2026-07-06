"""
Mini Project: Number Guessing Game

See README.md in this folder for the full spec. Fill in the TODOs.
"""

import random


def play_round(lower=1, upper=100):
    """Play one round of the guessing game. Returns the number of
    attempts taken, or None if the player quit early."""
    secret = random.randint(lower, upper)
    attempts = 0

    # TODO: implement the game loop
    # - prompt the player for a guess
    # - handle "quit"
    # - handle invalid (non-numeric) input with continue
    # - compare guess to secret with if/elif/else
    # - give a hint every 3 wrong guesses
    # - break on correct guess

    return attempts


if __name__ == "__main__":
    print("Guess the number between 1 and 100 (or type 'quit' to exit).")
    result = play_round()
    # TODO: print a summary based on the result
