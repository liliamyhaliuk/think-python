'''
Exercises of the book "Think python"
5.14.1 Exercise:
'''
# The time module provides a function, also named time, that returns the current Greenwich
# Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX
# systems, the epoch is 1 January 1970.
# 
# >>> import time
# >>> time.time()
# 1437746094.5735958
# Write a script that reads the current time and converts it to a time of day in hours, minutes,
# and seconds, plus the number of days since the epoch

import time

# Get current time in secinds since the epoch
current_time = time.time()
# Get amount of days since  the epoch (86400 - amount of seconds in 1 day)
days = int(current_time //  86400)

# Get amount of hours in the current day (3600 - amount of seconds in 1 hour)
hours = int((current_time % 86400) // 3600)

# Get amount of minutes in the current day
minutes = int(((current_time % 86400) % 3600) // 60)

# Get amount of seconds in the current day
seconds = int(((current_time % 86400) % 3600) % 60)

print(f"{days} days {hours} hours {minutes} minutes {seconds} seconds since the Epoch time")

# I suppose that time.time() returns time in UTC+0
from datetime import datetime, timezone
now = datetime.now(timezone.utc)
print(f"Current UTC Time: {now}")
