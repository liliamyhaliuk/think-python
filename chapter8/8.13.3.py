'''
Exercises of the book "Think python"
8.13.3 Exercise:
'''
# A string slice can take a third index that specifies the “step size”; that is, the number of
# spaces between successive characters. A step size of 2 means every other character; 3 means
# every third, etc.
# 
# >>> fruit = 'banana'
# >>> fruit[0:5:2]
# 'bnn'
# A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed
# string.
# 
# Use this idiom to write a one-line version of is_palindrome from Exercise 3.

def is_palindrome(inp_word):
    """Function checks if the reversed word looks the same as a word"""

    return inp_word == inp_word[::-1]

print(is_palindrome("noon"))
print(is_palindrome("cake"))
