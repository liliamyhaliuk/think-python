'''
Exercises of the book "Think python"
8.13.5 Exercise:
'''

# A Caesar cypher is a weak form of encryption that involves “rotating” each letter by a fixed
# number of places. To rotate a letter means to shift it through the alphabet, wrapping around
# to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
# 
# To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7
# is “jolly” and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the
# ship computer is called HAL, which is IBM rotated by -1.
# 
# Write a function called rotate_word that takes a string and an integer as parameters, and
# returns a new string that contains the letters from the original string rotated by the given
# amount.
# 
# You might want to use the built-in function ord, which converts a character to a numeric
# code, and chr, which converts numeric codes to characters. Letters of the alphabet are
# encoded in alphabetical order, so for example:
# 
# >>> ord('c') - ord('a')
# 2
# Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper
# case letters are different.

def rotate_word(word, number):
    """Function rotates word by using Caesar cypher"""

    low_word = word.lower()
    new_word = ""
    for letter in low_word:
        new_word += chr(ord(letter) + number)
    return f"New string: {new_word}. Old_string: {word}"

print(rotate_word("cheer", 7))
