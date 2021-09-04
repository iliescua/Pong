from turtle import Turtle, left
import random as rand

TOP_BORDER = 280

class Ball:


    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.pu()
        self.ball.color("white")
        self.x_move = 10
        self.y_move = 10
        self.r_score = 0
        self.l_score = 0 
    

    def move(self):
        x_dir = self.ball.xcor() + self.x_move
        y_dir = self.ball.ycor() + self.y_move
        self.ball.goto(x_dir, y_dir)

    
    def bounce(self, r_pad, l_pad):
        if self.ball.ycor() > TOP_BORDER or self.ball.ycor() < -TOP_BORDER:
            self.y_move *= -1

        check_right = self.ball.distance(r_pad) < 50 and self.ball.xcor() > 320
        check_left = self.ball.distance(l_pad) < 50 and self.ball.xcor() < -320

        if check_right or check_left:
            self.x_move *= -1


    def reset_ball(self):
        self.ball.goto(0,0)
        self.x_move *= -1

    def update_score(self):
        if  self.ball.xcor() > 380:
            self.r_score += 1
            self.reset_ball()

        if  self.ball.xcor() < -380:
            self.l_score += 1
            self.reset_ball()