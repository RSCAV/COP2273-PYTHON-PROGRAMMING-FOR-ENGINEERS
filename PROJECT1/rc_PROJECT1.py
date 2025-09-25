# File: rc_Project1.py
# Description: Plays the Bulls & Cows game using a helper module.
# Inputs:  Difficulty level (1-3), repeated guesses (or 'quit'), play again (y/n).
# Outputs: Bulls/Cows counts each turn, win/lose messages, and goodbye.
# By: Rodrigo Casanova-Aleman
#
# Three things I learned from Project 1:
# 1) How to write a separate module and import its functions.
# 2) How to validate user input with loops and simple checks.
# 3) How to use random numbers and pass data between functions (no globals).

import bulls_cows  # our module


def play_one_game() -> None:

    allowed_guesses = bulls_cows.get_difficulty()
    secret = bulls_cows.get_secret_code()

    # Uncomment this line while testing if you want to see the secret:
    # print("[debug] secret:", secret)

    guesses_left = allowed_guesses

    while guesses_left > 0:
        guess = bulls_cows.get_guess()
        if guess == "quit":
            return  # end this game immediately

        bulls = bulls_cows.get_num_bulls(guess, secret)
        cows = bulls_cows.get_num_cows(guess, secret)

        print("Bulls:", bulls)
        print("Cows:", cows)

        if bulls == 4:
            print("YOU WIN!")
            return

        guesses_left -= 1
        print(f"You have {guesses_left} guesses left.")

    # ran out of guesses
    print(f"YOU LOSE, the correct code was {secret}")


def main() -> None:
    print("Welcome to Bulls and Cows!")

    again = "y"
    while again and again[0].lower() == "y":
        play_one_game()
        again = input("\nWould you like to play again? (y/n): ")

    print("\nThank you for playing. Goodbye!")


if __name__ == "__main__":
    main()
