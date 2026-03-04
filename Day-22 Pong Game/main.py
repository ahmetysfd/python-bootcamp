from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    ball.move_ball()
    screen.update()
    time.sleep(0.01)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 20 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
#detect if paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()
