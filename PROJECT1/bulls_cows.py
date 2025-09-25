# bulls_cows.py
# This is a module (toolbox) used by the main Bulls & Cows game.
"""
bulls_cows module: helper functions for the Bulls & Cows game.
"""

import random

# show 3 levels of difficulty, keep askining until user enters 1/2/3, then return how many guesses.
def get_difficulty():
    """Show difficulty choices; keep prompting until valid; return allowed guesses."""
    print("\nDifficulty levels")
    print("1 - easy (12 guesses)")
    print("2 - medium (8 guesses)")
    print("3 - hard (5 guesses)")

    while True: 
        choice = input("\nChoose a difficulty level (1-3): ")
        if choice == "1":
            return 12
        elif choice == "2":
            return 8
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Try again.")
    
# Define get_guess() function: Ask for a guess or "quit". a valid guess is 4 unique digits.
def get_guess():
    """Ask for 'quit' or a valid 4-unique-digit guess; keep asking until valid; return string."""
    while True:
        raw = imput("\nGuess a 4-unique-digit-code (or type 'quit' to quit the game): ").strip()
        if raw.lower() == "quit":
            return "quit"
        
        if len(raw) != 4 or not raw.isdigit():
            print("Invalid code. Try again.")
            continue

        if len(set(raw)) != 4:
            print("Invalid code. Try again.")
            continue

        return raw

# Define get_secret_code() function: return a random 4-unique-digit string
def get_secret_code():
    """Return a random 4-unique-digit code string (no leading zero)."""
    digits = []

    first = random.randint(1, 9)
    digits.append(str(first))

    while len(digits) < 4:
        d = random.randint(0, 9)
        if str(d) not in digits:
            digits.append(str(d))
    
    return "".join(digits)

# Define get_num_bulls() function: return number of bulls (correct digit and position)
def get_num_bulls(guess, secret):
    """Return number of bulls (correct digit and position) between guess and secret."""
    bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
    return bulls

# Define get_num_cows() function: return number of cows (correct digit, wrong position)
def get_num_cows(guess, secret):
    """Return number of cows (correct digit, wrong position) between guess and secret."""
    cows = 0
    for i in range(4):
        if guess[i] in secret and guess[i] != secret[i]:
            cows += 1
    return cows


