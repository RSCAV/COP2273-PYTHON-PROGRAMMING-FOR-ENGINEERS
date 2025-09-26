"""
bulls_cows module

Required functions:
- get_difficulty()
- get_guess()
- get_secret_code()
- get_num_cows(guess, secret)
- get_num_bulls(guess, secret)
"""

import random

def get_difficulty() -> int:
    """Show the 3 difficulty levels; keep prompting until valid; return allowed guesses."""
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


def get_guess() -> str:
    """Prompt for a 4-unique-digit code (or 'quit'); keep prompting until valid."""
    while True:
        g = input("\nGuess a 4-unique-digit-code (or type 'quit' to quit the game): ").strip()
        if g.lower() == "quit":
            return "quit"

        if len(g) != 4 or not g.isdigit():
            print("Invalid code. Try again.")
            continue

        if len(set(g)) != 4:
            print("Invalid code. Try again.")
            continue

        return g


def get_secret_code() -> str:
    """Generate and return a random 4-unique-digit secret code as a string (no leading zero)."""
    digits = []
    first = random.randint(1, 9)          # avoid leading zero
    digits.append(str(first))
    while len(digits) < 4:
        d = random.randint(0, 9)
        if str(d) not in digits:
            digits.append(str(d))
    return "".join(digits)


def get_num_bulls(guess: str, secret: str) -> int:
    """Return number of bulls (right digit, right position)."""
    bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
    return bulls


def get_num_cows(guess: str, secret: str) -> int:
    """Return number of cows (right digit, wrong position)."""
    cows = 0
    for i in range(4):
        if guess[i] != secret[i] and (guess[i] in secret):
            cows += 1
    return cows