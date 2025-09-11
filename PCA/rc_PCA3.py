# File: ks_PCA3.py
# Description: Program that prints a 2D pattern orientated in 3 different directions depending on user input
# Input(s): Orientation choice (1, 2, or 3)
# Output(s): 2D pattern printed in chosen orientation
# By: Rodrigo Casanova (writer), Rocco Meyerholtz (observer)
# Three things I learned:
# 1: How to use nested loops to create 2D patterns.
# 2: How to implement input validation in a loop.
# 3: How to use conditional statements to control output formatting.

print("Let's print a 2D pattern in 3 different orientations!")

while True:
    # Get orientation choice from user with validation
    while True:
        choice = int(input("Choose an option (1, 2, 3): "))
        if choice == 1 or choice == 2 or choice == 3:
            break
    
    # Pattern 1: Print '*' where row >= col
    if choice == 1:
        for row in range(5):
            for col in range(5):
                if row >= col:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print() 

    # Pattern 2: Print '*' where row + col <= 4
    elif choice == 2:
        for row in range(5):
            for col in range(5):
                if row + col <= 4:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print() 

    # Pattern 3: Print '*' where col >= row
    elif choice == 3:
        for row in range(5):
            for col in range(5):
                if row + col >= 4:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print() 

    print()  

    # Ask if user wants to repeat
    repeat = input("Repeat the program? (y/n): ")

    if repeat == 'y' or repeat == 'Y':
        print()
        continue
    else:
        print("Thank you for using the program. Good bye!")
        break