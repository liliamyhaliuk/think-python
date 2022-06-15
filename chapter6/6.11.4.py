'''
Exercises of the book "Think python"
6.11.4 Exercise:
'''

# A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function
# called is_power that takes parameters a and b and returns True if a is a power of b. Note: you
# will have to think about the base case.

def is_power(a, b):
    """Function checks if a is a power of b"""
    if a == b:
        return True
    if b == 0:
        return False
    elif a == 0:
        return True
    elif a % b == 0 and is_power(a / b, b):
        return True
    else:
        return False

print(is_power(144, 11))
