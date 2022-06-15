'''
Exercises of the book "Think python"
6.11.5 Exercise:
'''

# The greatest common divisor (GCD) of a and b is the largest number that divides both of
# them with no remainder.
# 
# One way to find the GCD of two numbers is based on the observation that if r is the
# remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use
# gcd(a, 0) = a.
# 
# Write a function called gcd that takes parameters a and b and returns their greatest common
# divisor.
# 
# Credit: This exercise is based on an example from Abelson and Sussman’s Structure and
# Interpretation of Computer Programs.

def gcd(a, b):
    """Function returns the greatest common devisior of two parameters"""

    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(8, 16))
