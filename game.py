# game.py

import random

def generate_random_number(start=1, end=100):
    """Generates a random number between start and end (inclusive)."""
    return random.randint(start, end)

def check_guess(secret, guess):
    """Compares guess to secret number and returns feedback."""
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"
