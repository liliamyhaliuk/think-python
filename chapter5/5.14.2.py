'''
Exercises of the book "Think python"
5.14.2 Exercise:
'''
# Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
#                       an + bn = cn
# for any values of n greater than 2.
# 
# 1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
#    checks to see if Fermat’s theorem holds. If n is greater than 2 and
#                   a**n + b**n = c**n
#    the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program
#    should print, “No, that doesn’t work.”
# 
# 2. Write a function that prompts the user to input values for a, b, c and n, converts them to
#    integers, and uses check_fermat to check whether they violate Fermat’s theorem.

def check_format(a, b, c, n):
    """Function checks if the Fermat's Last Theorem is right"""

    if n > 2 and (a**n + c**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def test_theorem():
    """Functions converts user's input to the right format and checks Fermat's Theorem"""
    
    print("Check if the Fermat's Last Theorem is right!")

    # Get user's values
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    n = int(input("Enter n: "))
    check_format(a, b, c, n)

test_theorem()
