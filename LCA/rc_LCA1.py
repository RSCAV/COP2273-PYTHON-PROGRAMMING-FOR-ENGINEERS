# File: rc_LCA1.py
# Description: Warm-up exercise for COP2273
# Input(s): Classroom number for course requirement
#           2 integers 
#           One integer for displaying 'Go Gators!'
# Output(s): A course requirement message with course 
#            Result of the sumer of the two inputed integers
#            Multiple 'Go Gators!' based on user input
# By: Rodrigo Casanova-Aleman
#
# Three things I learned:
# 1. Learned how to structure a Python script with comments and sections.
# 2. Learned how to use input() and print() functions effectively.
# 3. Learned how to define and call a main() function in Python.

# define main() function
def main():
    # print welcome message
    print("Welcome to COP2273!")
    print()
    print("It's time for us to do our first in-class livecoding.")

    # get user input for classroom number
    classroom = input("Enter a classroom: ")

    # print course requirement message
    print("You are required to be in", classroom, "on Monday and")
    print("Wednesday every week!")

    # get user input for two integers
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    
    # calculate the sum of the two integers
    sum = num1 + num2

    # print the result of the sum
    print("The sum of the two integers is:", sum)

    # get user input for number of times to print 'Go Gators!'
    howmany = int(input("How many times you like to print 'Go Gators!'? "))

    # print 'Go Gators!' the specified number of times
    for i in range(howmany):
        print("Go, Gators!")

# Call main() function
main()