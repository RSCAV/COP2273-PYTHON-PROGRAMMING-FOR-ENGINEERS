# File: rc_LCA2.py
# Description: Compute the sum and the sum of cubes of the first N natural numbers
# Input(s): Integer N (prompted from the user)    
# Output(s): Sum from 1..N and sum of cubes from 1..N 
# By: Rodrigo Casanova-Aleman
#
# Three things I learned:
# 1. How to define and call functions that return values.
# 2. How to use loops to compute sums.
# 3. How to format output using f-strings.

# define sumN() function
def sumN(n: int) -> int:
    """Return the sum of the first n natural numbers using a loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# define sumNCubes() function
def sumNCubes(n: int) -> int:
    """Return the sum of cubes of the first n natural numbers using a loop."""
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total

# define main() function
def main() -> None:
    print("Let's compute the sum and sum of cubes of the first N natural numbers!")
    n = int(input("Enter a value for N: "))
    s = sumN(n)
    c = sumNCubes(n)
    print(f"The sum from 1 to {n} is {s}.")
    print(f"The sum of the cubes of those numbers is {c}.")

# Call main() function
if __name__ == "__main__":
    main()