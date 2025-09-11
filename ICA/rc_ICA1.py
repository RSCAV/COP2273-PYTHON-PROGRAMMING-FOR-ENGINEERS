# File: rc_ICA1.py
# Description: This program calculates an employee’s paycheck after deducting taxes.
# Input(s): Hourly wage, number of hours worked, tax percentage (max 15%)
# Output(s): Paycheck amount after tax deduction
# By: Rodrigo Casanova-Aleman
#
# Three things I learned:
# 1. Learned how to perform arithmetic operations in Python.
# 2. Learned how to convert string input to float for calculations.
# 3. Learned how to format output messages with variables.
#
# define main() function
def main():
    # Print welcome message
    print("Welcome to Wage Calculator!")

    # Get inputs from the user
    hourly_rate = float(input("How much do you get paid an hour? "))
    hours_worked = float(input("How many hours did you work? "))
    tax_rate = float(input("How much are your taxes? (Max 15%) "))

    # Calculate gross pay
    gross_pay = hourly_rate * hours_worked

    # Calculate tax deduction
    tax_amount = gross_pay * (tax_rate / 100)

    # Final paycheck
    net_pay = gross_pay - tax_amount

    # Print paycheck with 2 decimal places
    print(f"Your paycheck will be ${net_pay:.2f} after taxes!")

# call main() function
main()
