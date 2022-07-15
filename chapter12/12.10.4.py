'''
Exercises of the book "Think python"
12.10.4 Exercises:
'''

# Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
# 
# What is the longest English word, that remains a valid English word, as you remove
# its letters one at a time?
# Now, letters can be removed from either end, or the middle, but you can’t rearrange
# any of the letters. Every time you drop a letter, you wind up with another English
# word. If you do that, you’re eventually going to wind up with one letter and that too
# is going to be an English word—one that’s found in the dictionary. I want to know
# what’s the longest word and how many letters does it have?
# 
# I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
# you take a letter off, one from the interior of the word, take the r away, and we’re
# left with the word spite, then we take the e off the end, we’re left with spit, we take
# the s off, we’re left with pit, it, and I.
# 
# 
# Write a program to find all words that can be reduced in this way, and then find the longest
# one.
# 
# This exercise is a little more challenging than most, so here are some suggestions:
# 
#     1. You might want to write a function that takes a word and computes a list of all the
#         words that can be formed by removing one letter. These are the “children” of the word.
#     2. Recursively, a word is reducible if any of its children are reducible. As a base case, you
#         can consider the empty string reducible.
#     3. The wordlist I provided, words.txt, doesn’t contain single letter words. So you might
#         want to add “I”, “a”, and the empty string.
#     4. To improve the performance of your program, you might want to memoize the words
#         that are known to be reducible.
# Solution: http://thinkpython2.com/code/reducible.py.

import os

PATH = os.path.sep.join(['chapter12', 'words.txt'])

# Make dict from word list
with open(PATH, 'r') as f:

    word_list = {}
    for key in f:
        # Convert list into dict
        key = key.strip().lower()
        word_list.setdefault(key, "")

def make_reduced_words(word_dict):
    """The function makes dict with all reducable words"""

    reduced_words = {}

    for word in word_dict:
        for i in range(len(word)):

            # Make new word by reducing 1 letter (letter by letter)
            new_word = word[:i] + word[i+1:]
            if word_dict.get(new_word) is not None:

                # Add new word if it exists
                reduced_words.setdefault(word, [])
                reduced_words.get(word).append(new_word)
    return reduced_words


def check_if_reducable(word):
    """The function checks if the word is reducable"""

    if word == "i" or word == "":
        return True

    # Get list of all possible words from this word
    new_reduced = reduced_list.get(word)

    if new_reduced is not None:

        # Check nested list of reduced words
        for n_word in new_reduced:
            return check_if_reducable(n_word)
    return False

reduced_list = make_reduced_words(word_list)

result = []

# Check all words if they are reducable
for i in word_list:

    if reduced_list.get(i) is not None:
        if check_if_reducable(i):

            # Get all reducable words
            result.append(i)

# Get longest reducable word
sorted_result = sorted(result, key = len, reverse = True)
print(sorted_result[0])
