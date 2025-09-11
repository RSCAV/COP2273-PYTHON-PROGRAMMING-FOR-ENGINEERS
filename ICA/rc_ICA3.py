
# File: rc_ICA3.py
# Description: Program to calculate babysitting bill based on start and end times.
# Input(s): Start time (hours and minutes), End time (hours and minutes)
# Output(s): Total payment due, rounded to 2 decimal places
# By: Rodrigo Casanova-Aleman
#
# Three things I learned:
# 1. How to define and call functions in Python.
# 2. How to use the math library for trigonometric functions and converting degrees to radians.
# 3. How to format floating-point output to a specific number of decimal places.

print("Welcome to Babysitting Bill Calculator!")

while True:
	print("Enter times using 24 hour format (e.g. 7:30 PM is 19:30)")
	
	start_hour = int(input("Enter starting hours: "))
	start_min = int(input("Enter starting minutes: "))
	end_hour = int(input("Enter ending hours: "))
	end_min = int(input("Enter ending minutes: "))

	# Convert times to total minutes
	start_total = start_hour * 60 + start_min
	end_total = end_hour * 60 + end_min

	# Handle overnight (if end time is after midnight but before 6:00 AM, add 24*60)
	if 0 <= end_hour < 6:
		end_total += 24 * 60

	# 9:00 PM in minutes
	nine_pm = 21 * 60

	# Calculate payment
	if end_total <= nine_pm:
		# All before 9 PM
		total_minutes = end_total - start_total
		payment = (total_minutes / 60) * 13.50
	elif start_total >= nine_pm:
		# All after 9 PM
		total_minutes = end_total - start_total
		payment = (total_minutes / 60) * 9.45
	else:
		# Spans across 9 PM
		before_9pm = nine_pm - start_total
		after_9pm = end_total - nine_pm
		payment = (before_9pm / 60) * 13.50 + (after_9pm / 60) * 9.45

	print(f"Total payment due: ${payment:.2f}")

	repeat = input("Repeat the program? (y/n) ")
	if repeat.lower() != 'y':
		print("Thank you for using the program. Goodbye!")
		break

