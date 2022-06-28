'''
Exercises of the book "Think python"
10.15.12 Exercise:
'''
# Two words “interlock” if taking alternating letters from each forms a new word. For
# example, “shoe” and “cold” interlock to form “schooled”. Solution:
# http://thinkpython2.com/code/interlock.py. Credit: This exercise is inspired by an
# example at http://puzzlers.org.
# 
# 1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all
# pairs!
# 2. Can you find any words that are three-way interlocked; that is, every third letter forms
# a word, starting from the first, second or third?

import bisect
import os

def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word

def interlock(words):

    for word1 in words:
        if word1 == "":
            continue
        for word2 in words:
            if word2 == "" or word1 == word2:
                continue

            # Create interlock from 2 words
            index = 0
            new_word = ""
            while True:
                # Make new word by taking 1 letter from each word
                new_word += word1[index] + word2[index]

                # Move to the next letter
                index += 1

                # If out of index range (In case word1 is shorter)
                if index > len(word1) - 1:
                    if index > len(word2) - 1:
                        break
                    else:
                        new_word += word2[index]
                        break
                # If out of index range (In case word2 is shorter)
                if index > len(word2) - 1:
                    if index > len(word1) - 1:
                        break
                    else:
                        new_word += word1[index]
                        break

            # Check if the interlock exists in the list of words
            if in_bisect_cheat(words, new_word):
                print(word1, word2)

# Get the path to the file words.txt
path = os.path.sep.join(["chapter10", "words.txt"])

# Create a list of words from file words.txt
words = []
with open(path, "r") as f:
    for i in f:
        words.append(f.readline().strip())
words.sort()

interlock(words)
