# File: rc_project1.py
# Description: Program to play Bulls and Cows using the bulls_cows module
# Inputs: Difficulty level (1-3), repeated guesses (or "quit"), play again (y/n).
# Outputs: Bulls/Cows counts each turn, win/lose messages, goodbye.
# By: Rodrigo Casanova-Aleman
#
# Three things I learned from Project 1:
# 1) How to write and import a seperate module with functions.
# 2) How to use loops and conditionals effectively.
# 3) How to validate user input robustly.

# need to import the bulls_cows module
import rc_bulls_cows

# main function to run the game
def main():
    print("Welcome to Bulls and Cows!")

    again = "y"
    while again[0].lower() == "y":
        
        # choose difficulty and get number of allowed guesses
        allowed_guesses = rc_bulls_cows.get_difficulty()

        # make a new secret code for this game
        secret = rc_bulls_cows.get_secret_code()

        guesses_left = allowed_guesses
        won = False
        quit_round = False

        # guessing loop
        while guesses_left > 0:
            guess = rc_bulls_cows.get_guess()
            if guess == "quit":
                quit_round = True
                break

            bulls = rc_bulls_cows.get_num_bulls(guess, secret)
            cows = rc_bulls_cows.get_num_cows(guess, secret)

            print("Bulls:", bulls)
            print("Cows:", cows)

            if bulls == 4:
                print("YOU WIN!")
                won = True
                break

            guesses_left -= 1
            print(f"You have {guesses_left} guesses left.")

        # end-of-round messages
        if not won and not quit_round and guesses_left == 0:
            print(f"YOU LOSE, the correct code was {secret}")

        # ask to play again
        again = input("\nWould you like to play again? (y/n): ")

    print("\nThank you for playing. Goodbye!")

if __name__ == "__main__":
    main()