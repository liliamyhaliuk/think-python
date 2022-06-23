'''
Exercises of the book "Think python"
9.7.8 Exercise:
'''

import itertools

numbers = '0123456789'

possible_combinations = itertools.combinations(numbers, 6)
for num in range(0, 1000000):
    number = str(num) + str("0" * (6 - len(str(num))))

    # Check last 4 digits for palindrom
    if number[2:] == number[2:][::-1]:
        number = str(num + 1) + str("0" * (6 - len(str(num))))

        # Check last 5 digits for palindrom
        if number[1:] == number[1:][::-1]:
            number = str(num + 2) + str("0" * (6 - len(str(num))))

            # Check middle 4 digits for palindrom
            if number[1:5] == number[1:5][::-1]:
                number = str(num + 3) + str("0" * (6 - len(str(num))))

                # Check all digits for palindrom
                if number == number[::-1]:
                    print("This can be odometer: ", num)
