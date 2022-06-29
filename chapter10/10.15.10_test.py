'''
Exercises of the book "Think python"
10.15.10 Exercise:
'''
# To check whether a word is in the word list, you could use the in operator, but it would be
# slow because it searches through the words in order.
# 
# Because the words are in alphabetical order, we can speed things up with a bisection search
# (also known as binary search), which is similar to what you do when you look a word up in
# the dictionary (the book, not the data structure). You start in the middle and check to see
# whether the word you are looking for comes before the word in the middle of the list. If so,
# you search the first half of the list the same way. Otherwise you search the second half.
# 
# Either way, you cut the remaining search space in half. If the word list has 113,809 words, it
# will take about 17 steps to find the word or conclude that it’s not there.
# 
# Write a function called in_bisect that takes a sorted list and a target value and returns True
# if the word is in the list and False if it’s not.
# 
# Or you could read the documentation of the bisect module and use that! Solution:
# http://thinkpython2.com/code/inlist.py.

import os

def in_bisect(list_in, target):
    """Function search for the target in the list of words by using bisecting search"""

    middle = len(list_in) // 2
    last_middle = -1
    index = 0
    while last_middle != middle and 0 < middle <= len(list_in) - 1 :
        last_middle = middle

        if list_in[middle] == target:
            return True
        # Search in the first half
        if target[index] < list_in[middle][index]:
            middle = middle // 2
        # Search in the second half
        elif target[index] > list_in[middle][index]:
            step = (((len(list_in) - 1) - middle) // 2)
            if step == 0:
                middle += 1
            else:
                middle += step
        # Compare next letter if letters are the same
        elif target[index] == list_in[middle][index]:
            index += 1

        if last_middle == middle:
            break
    return False

# My test cases
print("My list. Works fine (not gound) - >", in_bisect(["aaa", "bbb", "ccc", "dddd", "eeeet"], "eeee"))
print("My list. Works fine (found) - > ", in_bisect(["aaa", "bbb", "ccc", "dddd", "eeee"], "eeee"))


# Real test case. Words copied from list of words
test_words = ['zananas', 'zanders', 'zanies', 'zanily', 'zaninesses']
print("Words from words.txt. Doesn't work ->",in_bisect(test_words, 'zananas'))

# Create a list of words from file words.txt

path = os.path.sep.join(["chapter10", "words_test.txt"])

words = []
with open(path, "r") as f:
    for i in f:
        words.append(f.readline().strip())
words.sort()
#print(words)

# Real test case. Words from words.txt
print("Words from words.txt. Doesn't work ->", in_bisect(words, "zananas" ))
