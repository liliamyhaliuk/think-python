'''
Exercises of the book "Think python"
7.9.3 Exercise:
'''

# The mathematician Srinivasa Ramanujan found an infinite series that can be used to
# generate a numerical approximation of 1 / π:
#  
# Write a function called estimate_pi that uses this formula to compute and return an estimate
# of π. It should use a while loop to compute terms of the summation until the last term is
# smaller than 1e-15 (which is Python notation for 10−15). You can check the result by
# comparing it to math.pi.

import math

def factorial(num):
    """The function compute factorial of a passed number"""

    if num == 0:
        return 1
    else:
        fact = factorial(num - 1)
        res = num * fact
        return res

def estimate_pi():
    """The function compute an estimate number of pi"""

    # Left part of the expression
    expr_1 = (2 * math.sqrt(2)) / 9801

    k = 0

    summ = 0

    # Continue until the last term smaller than 1e-15
    while True:

        # Compute expression above in current term
        expr_2_above = factorial(4 * k) * (1103 + (26390 * k))

        # Compute expression under in current term
        expr_2_under = (factorial(k)**4) * (396**(4 * k))

        # Compute the whole expression in the current term
        expr_2 = expr_2_above / expr_2_under

        summ +=expr_2

        term = expr_1 * expr_2

        if abs(term) < 10**(-15):
            break

        k += 1
    # Get number pi
    number_pi = 1 / (expr_1 * summ)

    return number_pi

print(f"Real pi number: {math.pi}. Function return: {estimate_pi()}")
