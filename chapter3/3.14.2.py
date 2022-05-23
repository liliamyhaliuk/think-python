'''
Exercises of the book "Think python"
3.14.2 Exercises:
'''

# 1. Type this example into a script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
# 3. Copy the definition of print_twice from earlier in this chapter to your script.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
# 5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. 
#    There should be only two statements in the body of this function, not four.

def do_twice(f, v):
    """Run a function two times with an argument v"""
    f(v)
    f(v)

def print_spam(s):
    print(s)

def do_four(func, val):
    """Run a function four times with an argument val"""
    do_twice(func, val)
    do_twice(func, val)

do_four(print_spam, 'spam')
