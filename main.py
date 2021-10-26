from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(-350, 0)
paddle_2 = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle_1.go_up, "w")
screen.onkey(paddle_1.go_down, "s")
screen.onkey(paddle_2.go_up, "Up")
screen.onkey(paddle_2.go_down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 320 or ball.distance(paddle_1) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        print("WE HIT")

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_p2_score()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_p1_score()


screen.exitonclick()
