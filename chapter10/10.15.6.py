'''
Exercises of the book "Think python"
10.15.6 Exercise:
'''
# Two words are anagrams if you can rearrange the letters from one to spell the other. Write a
# function called is_anagram that takes two strings and returns True if they are anagrams.

def is_angram(word1, word2):
    """Function checks if words are anagrams"""

    # False if words have not the same lenght
    if len(word1) != len(word2):
        return False
  
    # Check each letter if it is in the word2
    for letter in word1:
        if word1.count(letter) != word2.count(letter):
            return False
    return True
# True
print(is_angram("noon", "onon"))
# False 
print(is_angram("noon", "onont"))
# False
print(is_angram("noon", "ooon"))
