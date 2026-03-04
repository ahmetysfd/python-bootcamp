from random import randint
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make Your BET!", prompt="Which turtle will win the race Enter a color:")

all_turtles = []
colors = ["red", "orange", "blue", "green", "purple", "yellow"]
y_positions = [100, 60, 20, -20, -60, -100]

for turtle_index in range(0, 6):

    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(-210, y_positions[turtle_index])
    tim.color(colors[turtle_index])
    all_turtles.append(tim)


is_on = True

while is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the {winning_color} turtle is the winner")
            else:
                print(f"You've lost the {winning_color} turtle is the winner")

        random_distance = random.randint(1, 15)
        turtle.forward(random_distance)





screen.exitonclick()


