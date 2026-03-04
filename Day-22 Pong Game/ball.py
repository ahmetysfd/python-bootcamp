from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)


        # Ball movement speed
        self.dx = 2  # Instance variable
        self.dy = 2  # Instance variable


    def move_ball(self):
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

      # Reverse direction on top/bottom collision

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

