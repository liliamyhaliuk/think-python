'''
Exercises of the book "Think python"
7.9.1 Exercise:
'''

# Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that takes a as
# a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.
# 
# To test it, write a function named test_square_root that prints a table like this:
# 
# a   mysqrt(a)     math.sqrt(a)  diff
# -   ---------     ------------  ----
# 1.0 1.0           1.0           0.0
# 2.0 1.41421356237 1.41421356237 2.22044604925e-16
# 3.0 1.73205080757 1.73205080757 0.0
# 4.0 2.0           2.0           0.0
# 5.0 2.2360679775  2.2360679775  0.0
# 6.0 2.44948974278 2.44948974278 0.0
# 7.0 2.64575131106 2.64575131106 0.0
# 8.0 2.82842712475 2.82842712475 4.4408920985e-16
# 9.0 3.0           3.0           0.0
#
# The first column is a number, a; the second column is the square root of a computed with
# mysqrt; the third column is the square root computed by math.sqrt; the fourth column is the
# absolute value of the difference between the two estimates.


import math


def mysqrt(a):
    """The function compute the square root of a passed number"""

    # Choose the value of x
    x = a - a / 2

    # Approximate value of 'how close is close enough'
    epsilon = 0.0000001

    # Get square root of a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y


def test_mysqrt():
    """The function test mysqrt() and prints results"""
    # Headers for the output table
    print("a       mysqrt(a)         math.sqrt(a)        diff")
    print("-       ---------         ------------        ----")

    # Print results
    for a in range(1, 10):

        res_func = mysqrt(a)
        res_math = math.sqrt(int(a))
        diff = res_math - res_func

        space_1 = (19 - len(str(res_func))) * " "
        space_2 = (19 - len(str(res_math))) * " "

        print(f"{a}      {res_func}{space_1}{res_math}{space_2}{diff}")

test_mysqrt()
