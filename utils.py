# utils.py

def ask_to_play_again():
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    return choice == "y"
