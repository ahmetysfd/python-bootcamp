from turtle import Screen
import time
from snake2 import Snake
from food2 import Food
from scoreboard2 import ScoreBoard



screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My snake game")



snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with  food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #Detect Collision With Body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()