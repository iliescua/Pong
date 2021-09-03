from turtle import Screen
from paddle import Paddle

WIDTH = 800
HEIGHT = 600
START_X = 350
START_Y = 0

screen = Screen()
screen.title("Pong")
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

is_game_on = True
right_paddle = Paddle(START_X, START_Y)
left_paddle = Paddle(-START_X, START_Y)

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

while is_game_on:
    screen.update()

screen.exitonclick()