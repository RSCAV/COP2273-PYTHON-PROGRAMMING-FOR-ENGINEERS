# File: rc_LCA4.py
# Description: This program check whether an ISBN-13 number is valid or not.
# Input(s): An ISBN-13 number (prompted from the user)
# Output(s): Cbecking whether the given ISBN-13 number is valid or not
# By: Rodrigo Casanova-Aleman
#
# Three things I learned:
# 1. 
# 2. 
# 3.

# define is_valid_ISBN13()
def is_valid_ISBN13(isbn):
    # remopve hyphens or spaces from the ISBN-13 number
    isbn = isbn.replace("-", "")
    isbn = isbn.replace(" ", "")

    if len(isbn) != 13 or not(isbn.isdigit()):
        return False
    else:
        total = 0
        for i in range(len(isbn)):
            if (i+1) % 2 == 1: # odd position
                total = total + int(isbn[i]) * 1
            else: # even position
                total = total + int(isbn[i]) * 3
        return total % 10 == 0
    

# define main() function
def main():
    # welcome message
    print('Welcome to ISBN-13 Verifier!')

    again = 'y'
    while again and again[0].lower() == 'y':

        # print space
        print()

        # get user input for an ISBN-13 number
        isbn13 = input('Enter an ISBN-13: ')

        # check if the entered ISBN-13 number is valid or not and display the result
        if is_valid_ISBN13(isbn13) == True:
            print(isbn13, 'is valid!')
        else:
            print(isbn13, 'is not valid!')

        # ask to repeat or exit the program
        again = input('\nRepeat the program? (y/n): ')

    # goodbye message
    print ('\nThank you for using the program. Goodbye!')
    
# call main() function
if __name__ == "__main__":
    main()