'''
Exercises of the book "Think python"
4.12.3 Exercises:
'''

import turtle
import math

# Create 3 flowers
new_shape = turtle.Turtle()
#second_flow = turtle.Turtle()
#third_flow = turtle.Turtle()

def shape(t, n, lenght):
    """Draw a shape

    t: Object of class Turtle
    n: amount of pieces in shape
    lenght: the lenght of piece of shape
    """
    # Calculate the angle for the turn
    angle = (180 - (360 / n))/ 2

    # Calculate width of each piece of shape
    width = 2 * lenght * math.cos(math.radians(angle))

    # Draw n pieces of shape
    for i in range(n):
        t.fd(lenght)
        t.lt(180 - angle)
        t.fd(width)
        t.lt(180 - angle)
        t.fd(lenght)
        t.rt(180)
    # Move turtle to the right to for drawing the next shape
    t.pu()
    t.fd(lenght*2 + 10)
    t.pd()

shape(new_shape, 5, 30)
shape(new_shape, 6, 30)
shape(new_shape, 7, 30)

new_shape.hideturtle()
turtle.mainloop()
