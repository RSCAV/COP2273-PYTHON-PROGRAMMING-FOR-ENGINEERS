# File: rc_ICA2.py
# Description: Program to calculate the length of the unknown side of a triangle using the Law of Cosines.
# Input(s): Length of first side (a), length of second side (b), angle between them (in degrees)
# Output(s): Length of the unknown side (c), rounded to 4 decimal places
# By: Rodrigo Casanova-Aleman
#
# Three things I learned:
# 1.  How to define and call functions in Python.
# 2.  How to use the math library for trigonometric functions and converting degrees to radians.
# 3.  How to format floating-point output to a specific number of decimal places.

import math

# define function to calculate length of unknown side using Law of Cosines
def loc_cal(a, b, angle_deg):
    """
    Calculates the length of the unknown side using the Law of Cosines.
    a = length of first side
    b = length of second side
    angle_deg = angle (in degrees) between sides a and b
    """
    angle_rad = math.radians(angle_deg)  # convert degrees to radians
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2) - 2 * a * b * math.cos(angle_rad))
    return c

# main program
print("Welcome to Law of Cosines Calculator!")

# Get inputs from the user
a = float(input("What is the length of your first side (in centimeters)? "))
b = float(input("What is the length of your second side (in centimeters)? "))
angle = float(input("What is the angle between (in degrees)? "))

# Calculate the length of the unknown side
c = loc_cal(a, b, angle)
print(f"According to the Law of Cosines, the length of the unknown side is {c:.4f} centimeters!")