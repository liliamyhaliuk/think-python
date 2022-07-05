'''
Exercises of the book "Think python"
10.15.8 Exercise:
'''
# This exercise pertains to the so-called Birthday Paradox, which you can read about at
# http://en.wikipedia.org/wiki/Birthday_paradox.
# 
# If there are 23 students in your class, what are the chances that two of them have the same
# birthday? You can estimate this probability by generating random samples of 23 birthdays
# and checking for matches. Hint: you can generate random birthdays with the randint
# function in the random module.
# 
# You can download my solution from http://thinkpython2.com/code/birthday.py.


import math
import datetime
import random

# Calculation the chances of not having people with the same birthday
p_minus =  (math.factorial(365) / math.factorial(342)) * (1 / 365)**23

# Calculation of the chances tha two people from 23 will have the same birthday
prob = 1 - p_minus

print(f"The chances of 2 people to have the same birthday among 23 students are: {prob} %")

# Test function

def check_similarity(birthday, others):
    """The function checks amount of same birthdays among others"""

    similar = 0
    for i in others:
        if birthday == i:
            similar += 1

    return similar

def test_prob():
    """THe function count chances of having same birthday among 23 people"""

    # Generate 23 random birthdays
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2000, 7, 1)


    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    birthdays = []

    for i in range(23):

        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        birthdays.append(random_date)

    # Counter of people with same birthdays
    same_birthday = 0

    # Check random birthdays
    for birthday in birthdays:
        same_birthday += check_similarity(birthday, birthdays[birthdays.index(birthday) + 1 :])
    
    # Return amount of same birthdays
    return print(f"There are {same_birthday} people that have same birthday.")

# Test1
test_prob()

#Test2
test_prob()

#Test3
test_prob()
