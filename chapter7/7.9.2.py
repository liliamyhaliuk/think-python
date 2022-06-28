'''
Exercises of the book "Think python"
7.9.2 Exercise:
'''
# The built-in function eval takes a string and evaluates it using the Python interpreter. For example:
# 
# >>> eval('1 + 2 * 3')
# 7
# >>> import math
# >>> eval('math.sqrt(5)')
# 2.2360679774997898
# >>> eval('type(math.pi)')
# <class 'float'>
#
# Write a function called eval_loop that iteratively prompts the user, takes the resulting input
# and evaluates it using eval, and prints the result.
# 
# It should continue until the user enters 'done', and then return the value of the last
# expression it evaluated.


USER_INPUT = ""
expression = ""

# Continue until user enters 'done'
while True:

    # Get user input
    USER_INPUT = input("What operation would you like to evaluate?: ")

    if USER_INPUT == "done":
        break
    # Make a string from user's input
    expression += USER_INPUT

try:
    print("Result: ", eval(expression))
except ZeroDivisionError:
    print("You can't divide by zero!")
except SyntaxError:
    print("Expression isn't correct!")
except NameError:
    print("Variable in your expression doesn't exist!")
