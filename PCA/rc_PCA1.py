# File: rc_PCA1.py
# Description: Program to calculate the average and standard deviation of five input values.
# Input(s): first, second, third, fourth, fifth values (float)
# Output(s): Average of the five input values
#            Standard deviation of the five input values
# By: Rodrigo Casanova-Aleman (writer), Kanon Scarbinsky (observer)
#
# Three things I learned:
# 1. Learned how to calculate average and standard deviation.
# 2. Learned how to handle multiple float inputs.
# 3. Learned how to format output to two decimal places.

# define main() function
def main():

    # print welcome message
    print("Welcome to Average and Standard Deviation Calculator!")

    # inform user about entering five values
    print("You must enter 5 values!")

    # prompt for five values
    _1st_value = float(input("Enter the first value: "))
    _2nd_value = float(input("Enter the second value: "))
    _3rd_value = float(input("Enter the third value: "))
    _4th_value = float(input("Enter the fourth value: "))
    _5th_value = float(input("Enter the fifth value: "))

    # calculate and print the average and standard deviation
    average = (_1st_value + _2nd_value + _3rd_value + _4th_value + _5th_value) / 5
    standard_deviation = (((_1st_value - average) ** 2 + (_2nd_value - average) ** 2 + (_3rd_value - average) ** 2 + (_4th_value - average) ** 2 + (_5th_value - average) ** 2) / 4) ** 0.5
    
    print(f"The average of your datatset is {average:.2f} and the standard deviation is {standard_deviation:.2f}")

# Call main() function
main()