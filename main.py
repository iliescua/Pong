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
user_paddle = Paddle(START_X, START_Y)
comp_paddle = Paddle(-START_X, START_Y)

screen.listen()
screen.onkeypress(user_paddle.move_up, "Up")
screen.onkeypress(user_paddle.move_down, "Down")

while is_game_on:
    screen.update()

screen.exitonclick()