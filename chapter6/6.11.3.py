'''
Exercises of the book "Think python"
6.11.3 Exercise:
'''

# Write a function called is_palindrome that takes a string argument and returns True if
# it is a palindrome and False otherwise. Remember that you can use the built-in
# function len to check the length of a string.

def is_palindrome(word):
    """Function test the word if it is a palindrome or not"""
    return word == word[::-1]

print(is_palindrome("wow"))
print(is_palindrome("Liliia"))
