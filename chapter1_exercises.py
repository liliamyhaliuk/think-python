#Exercises of the book "Think python"
#1.8 Exercises

#Exercise 4
#"If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? 
#What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile)."

#distance in kilometers
distance = 10

#transform kilometers into miles
distance = 10/1.61

#time of race
full_time = 43.30

#average time per mile
avg_time = full_time/distance

print(avg_time)