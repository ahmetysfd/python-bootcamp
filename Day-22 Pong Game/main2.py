from turtle import Screen
from ball2 import Ball
from paddle2 import Paddle
import time

screen = Screen()
screen.setup(1200, 1000)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((550, 0))
l_paddle = Paddle((-550, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_on = True
while is_on:

    time.sleep(0.1)
    screen.update()
    ball.move_ball()


    #   Collision with wall
    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce()

    #Detect collision with right paddle

screen.exitonclick()