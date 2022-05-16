"""
 Exercises of the book "Think python"
 1.8 Exercises
"""

# Exercise 4
# 1. How many seconds are there in 42 minutes 42 seconds?
total_seconds = 42 * 60 + 42

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
full_distance = 10 / 1.61

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds,
#    what is your average pace (time per mile in minutes and seconds)?
#    What is your average speed in miles per hour?

# Average pace (time per mile in minutes and seconds)
avg_pace_sec = total_seconds / full_distance
avg_pace_min = avg_pace_sec // 60 + ((avg_pace_sec % 60) / 100)

print(avg_pace_sec)
print(avg_pace_min)

# Average speed in miles per hour
avg_speed = 3600 / avg_pace_sec

print(avg_speed)
