# main.py

from game import generate_random_number, check_guess
from utils import ask_to_play_again

def start_game():
    print(" Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100 ")

    secret_number = generate_random_number()
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            result = check_guess(secret_number, guess)
            print(result)

            if result == "Correct!":
                print(f" Congratulations! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print(" Please enter a valid number.")

if __name__ == "__main__":
    start_game()
