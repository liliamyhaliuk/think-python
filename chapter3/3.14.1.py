'''
Exercises of the book "Think python"
3.14.1 Exercises:
'''
# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces
# so that the last letter of the string is in column 70 of the display.

def right_justify(string):
    """Move argument to the left so the last letter of the argument is in column 70 of display"""
    left_space = 70 - len(string)
    print(left_space*' ' + string)

right_justify('s')
