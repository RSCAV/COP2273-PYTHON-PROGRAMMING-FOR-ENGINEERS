# File: rc_LCA3.py
# Description: This prgram calculates the additions, subtractions, multiplications, and divisions of two numbers entered by the user.
# Input(s): an option (1-4), two operands (prompted from the user)
# Output(s): a result of the chosen operation with the given two numbers and an 
# By: Rodrigo Casanova-Aleman
#
# Three things I learned:
# 1. How to import a module and use its functions. 
# 2. How to create a menu-driven program using loops and conditionals.
# 3. How to format floating-point output using f-strings.

# import arithmetic_operations module
import arithmetic_operations as ao
from arithmetic_operations import add, subtract, multiply, divide

# define main() function
def main():
    # welcome message
    print("Welcome to four-function calculator!")
    
    again = 'y'
    while (again == 'y'):
        # display menu
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        
        # get user input for an operation choice
        opt = int(input("Select an option: "))
        
        # get user input for two operands
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # perform the chosen operation and display the result
        if opt == 1:
            print(f"{num1} + {num2} = {add(num1, num2):.3f}")
        elif opt == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2):.3f}")
        elif opt == 3:
            print(f"{num1} * {num2} = {multiply(num1, num2):.3f}")
        else:  # opt == 4
            print(f"{num1} / {num2} = {divide(num1, num2):.3f}")
        
        # ask to repeat or exit the program
        again = input("Repeat the program? (y/n) ")
    
    # goodbye message
    print("Thank you for using the program. Goodbye!")

# Call main() function
if __name__ == "__main__":
    main()