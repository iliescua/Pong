from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_HEIGHT = 1
MOVE_AMNT = 20

class Paddle:


    def __init__(self, x, y):
        self.paddle = Turtle("square")
        self.paddle.pu()
        self.paddle.color("white")
        self.paddle.shapesize(STRETCH_WIDTH, STRETCH_HEIGHT)
        self.paddle.goto(x, y)


    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + MOVE_AMNT)


    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - MOVE_AMNT)


    def pad_position(self):
        return self.paddle.position()

    