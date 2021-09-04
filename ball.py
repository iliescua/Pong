from turtle import Turtle, left
import random as rand

TOP_BORDER = 280
SIDE_BORDER = 380
P_SIZE = 50
P_POSITION = 320

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

        check_right = self.ball.distance(r_pad) < P_SIZE and self.ball.xcor() > P_POSITION
        check_left = self.ball.distance(l_pad) < P_SIZE and self.ball.xcor() < -P_POSITION

        if check_right or check_left:
            self.x_move *= -1


    def reset_ball_right(self):
        self.ball.goto(0, 0)
        if self.x_move < 0:
            self.x_move *= -1

    
    def reset_ball_left(self):
        self.ball.goto(0, 0)
        if self.x_move > 0:
            self.x_move *= -1


    def update_score(self):
        if  self.ball.xcor() > SIDE_BORDER:
            self.l_score += 1
            self.reset_ball_right()

        if  self.ball.xcor() < -SIDE_BORDER:
            self.r_score += 1
            self.reset_ball_left()

    
    def get_r_score(self):
        return self.r_score


    def get_l_score(self):
        return self.l_score
