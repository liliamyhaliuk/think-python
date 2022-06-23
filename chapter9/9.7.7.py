'''
Exercises of the book "Think python"
9.7.7 Exercise:
'''

# This question is based on a Puzzler that was broadcast on the radio program Car Talk
# (http://www.cartalk.com/content/puzzlers):
# 
# Give me a word with three consecutive double letters. I’ll give you a couple of words
# that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
# would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
# p-p-i. If you could take out those i’s it would work. But there is a word that has three
# consecutive pairs of letters and to the best of my knowledge this may be the only
# word. Of course there are probably 500 more but I can only think of one. What is the
# word?
# Write a program to find it. Solution: http://thinkpython2.com/code/cartalk1.py.

import os

# Get a path to the file with all words in English
path = os.path.sep.join(["chapter9", "words.txt"])


# Open file with words
with open(path, 'r') as words:
   
    # Work with each word separately
    for i in words:
        word = words.readline().strip()
      
        # Skip all words with lenght smaller than 6
        if len(word) < 6:
            continue
        # Skip all words with lenght 6 and without first double
        if len(word) == 6 and word[0] != word[1]:
            continue

        # Get max index in the word
        index = len(word) - 1

        # Counter for amount of double letters
        double = 0

        # Iterate trought all letters
        while index >= 0:

            # Mark that you found double letter
            if word[index] == word[index-1]:

                # Count double
                if double > 0:
                    double +=1
                else:
                    double = 1

                # Skip next index since it's a double letter for current index
                index -= 1

                # Stop iterating if the word is the right one
                if double == 3:
                    break

            else:
                double = 0

            index -= 1
      
        # Show the word if you found the right one
        if double == 3:
            print(word)
            break
