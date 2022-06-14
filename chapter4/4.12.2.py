'''
Exercises of the book "Think python"
4.12.3 Exercises:
'''

import turtle
import math

# Create 3 flowers
flow = turtle.Turtle()


def flower(t, angl, quantity, fl_lenght):
    """Draw a flower

    t: Object of class Turtle
    angl: angle of the petal
    quantity: amount of petals
    fl_lenght: the lenght of flower in pixels
    """
    # Count the radius of the circle from the lenght of flower
    radius = (fl_lenght/2) **(0.5)

    # Calculate the lenght of circle 
    length = (2*radius*math.pi)/100

    # Calculate the angle fo the turn that turtle will make
    angle = angl/100

    for j in range(quantity):
        for i in range(100):
            t.fd(length)
            t.lt(angle)
        t.lt(180 - angl)
        for i in range(100):
            t.fd(length)
            t.lt(angle)
        t.rt(180 + ((angl*quantity - 360)/quantity))
    
    # Move to the right to for drawing the next flower
    t.pu()
    t.fd(100)
    t.pd()

flower(flow, 80, 10, 50)
flower(flow, 20, 30, 50)
flower(flow, 51.4, 7, 50)

turtle.mainloop()
