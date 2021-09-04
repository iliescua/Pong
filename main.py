from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
START_X = 350
START_Y = 0
SLEEP_TIME = 0.1

screen = Screen()
screen.title("Pong")
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

is_game_on = True
r_pad = Paddle(START_X, START_Y)
l_pad = Paddle(-START_X, START_Y)
ball = Ball()
sb = Scoreboard()

screen.listen()
screen.onkeypress(r_pad.move_up, "Up")
screen.onkeypress(r_pad.move_down, "Down")
screen.onkeypress(l_pad.move_up, "w")
screen.onkeypress(l_pad.move_down, "s")

while is_game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect collision with top border or paddles
    ball.bounce(r_pad.pad_position(), l_pad.pad_position())

    # Check for score updates and write score
    ball.update_score()
    sb.write_score(ball.get_r_score(), ball.get_l_score())


screen.exitonclick()