import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

sceen = Screen()
sceen.bgcolor("black")
sceen.setup(height=600, width=800)
sceen.title("pong")
sceen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
sceen.listen()

sceen.onkey(r_paddle.go_up, "Up")
sceen.onkey(r_paddle.go_down, "Down")
sceen.onkey(l_paddle.go_up, "w")
sceen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sceen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320  or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()


sceen.exitonclick()
