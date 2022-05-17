"""
Exercises of the book "Think python"
2.10 Exercises
"""
import math
import datetime

# Exercise 2
# Using the Python as a calculator

# 1. The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?
radius = 5

print("The volume of a sphere: ", (4 / 3 * math.pi * radius**3))


# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
#   Shipping costs $3 for the first copy and 75 cents for each additional copy.
#   What is the total wholesale cost for 60 copies?
cover_price = 24.95
discount = 0.4
copies_amount = 60


s_cost_first = 3  # Shipping_cost for the first copy
s_cost_add = 0.75  # Shipping_cost for each additional copy

# Total wholesale cost
sum = (
    (cover_price * (1 - discount)) * copies_amount
    + (s_cost_add * (copies_amount - 1))
    + s_cost_first
)
print("Total wholesale cost for 60 copies: ", round(sum, 2))


# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
#   then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
#   what time do I get home for breakfast?

# Speed (minutes)
easy_pace = "08:15"
tempo = "07:12"

def time_to_seconds(time: str):
    """Function convert time from str format('07:12', MM:SS) to amount of seconds."""
    return (int(time[: time.find(":")]) * 60) + (int(time[time.find(":") + 1 :]))

# Convert time to seconds
easy_pace = time_to_seconds(easy_pace)
tempo = time_to_seconds(tempo)

# Start time of the run
start_time = datetime.datetime.strptime("6:52", "%H:%M")

# Calculate duration of the run in seconds (miles*time per mile)
whole_time = 2 * easy_pace + 3 * tempo

# Calculate time of the end of the run
home_time = (start_time + datetime.timedelta(seconds=whole_time)).time()

print("You will get home at: ", home_time)
