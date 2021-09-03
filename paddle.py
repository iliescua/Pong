from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_HEIGHT = 1
MOVE_AMOUNT = 20

class Paddle:


    def __init__(self, x, y):
        self.paddle = self.generate_paddle(x, y)

    
    def generate_paddle(self, x, y):
        pad = Turtle("square")
        pad.pu()
        pad.color("white")
        pad.shapesize(STRETCH_WIDTH, STRETCH_HEIGHT)
        pad.goto(x, y)
        return pad


    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + MOVE_AMOUNT)


    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - MOVE_AMOUNT)