import turtle
from turtle import Turtle, Screen
import random

is_raced_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="take a guess which turtle will win the race", prompt="type your bet")
y_positions = [100, 60, 20, -20, -60, -100]
colors = ["red", "orange", "blue", "yellow", "purple", "green"]
all_turtles = []

for turtle_index in range(0, 6):

    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-210, y=y_positions[turtle_index])
    tim.color(colors[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_raced_on = True

while is_raced_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_raced_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the {winning_color} turtle is the winner")
            else:
                print(f"You've lost the {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
