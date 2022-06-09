'''
Exercises of the book "Think python"
4.12.4 Exercises:
'''

import turtle

letter = turtle.Turtle()
letter.pensize(5)

def draw_A(t):
    """Draw a letter A"""
    t.circle(50)

def draw_B(t):
    """Draw a letter B"""
    t.circle(25, 180)
    t.rt(180)
    t.circle(25, 180)
    t.lt(90)
    t.fd(100)

def draw_C(t):
    """Draw a letter C"""
    t.circle(25, 20)
    t.penup()
    t.lt(70)
    t.fd(50)
    t.lt(90)
    t.pendown()
    print()
    t.circle(25,200)
    

draw_C(letter)
