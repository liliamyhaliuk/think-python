'''
Exercises of the book "Think python"
5.14.3 Exercise:
'''

# If you are given three sticks, you may or may not be able to arrange them in a triangle. For
# example, if one of the sticks is 12 inches long and the other two are one inch long, you will
# not be able to get the short sticks to meet in the middle. For any three lengths, there is a
# simple test to see if it is possible to form a triangle:
# 
#     If any of the three lengths is greater than the sum of the other two, then you cannot
#     form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
#     form what is called a “degenerate” triangle.)
#
#     1. Write a function named is_triangle that takes three integers as arguments, and that
#        prints either “Yes” or “No”, depending on whether you can or cannot form a triangle
#        from sticks with the given lengths.
#     2. Write a function that prompts the user to input three stick lengths, converts them to
#        integers, and uses is_triangle to check whether sticks with the given lengths can form
#        a triangle

def is_triangle(a, b, c):
    """Function checks if 3 given sticks(a, b, c) can form a triangle"""
    
    # Check if any of the given values is greater than the sum of other two
    if a > (b+c) or b > (a + c) or c > (a + b):
        print("No")
    else:
        print("Yes")

def test_if_triangle():
    """Functions converts user's input to the right format and checks if values can form triangle"""

    print("Check if you can form triangle from the length of given sticks!")
    # Get user's values
    a = int(input("Enter the lenght of stick a: "))
    b = int(input("Enter the lenght of stick b: "))
    c = int(input("Enter the lenght of stick c: "))
    is_triangle(a, b, c)

test_if_triangle()
