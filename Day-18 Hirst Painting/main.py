import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy.speed("fastest")
timmy.circle(100)
timmy.penup()






screen.exitonclick()