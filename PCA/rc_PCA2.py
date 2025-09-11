# File: ks_PCA2.py
# Description: Converter between meters and feet using another python module
# Input(s): Prompt for a conversion selection
#           How many feet to convert
#           How many meters to convert
# Output(s): Feet to meters conversion or meters to feet conversion
# By: Kanon Scarbinsky (writer), Rodrigo Casanova-Aleman (observer)(absent)
# Three things I learned:
# 1: How to make my own module to import to another file
# 2: How to use an if statement with two different options
# 3: How to make a conversion from meters to feet

import conversions as cs

def main():
    print('Feet and Meters Converter')
    print('')
    print('Conversions Menu: ')
    print('a. Feet to Meters')
    print('b. Meters to feet')
    ab_input = str(input('Select a conversion: '))
    if ab_input == 'a':
        feet = float(input('Enter feet: '))
        meters = cs.to_meters(feet)
        print('{0:.2f} meters'.format(meters))
    else:
        meters = float(input('Enter meters: '))
        feet = cs.to_feet(meters)
        print('{0:.2f} feet'.format(feet))

main()