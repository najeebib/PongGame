from turtle import Screen, Turtle

sceen = Screen()
sceen.bgcolor("black")
sceen.setup(height=600, width=800)
sceen.title("pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)
sceen.listen()


def go_up():
    new_y = paddle.ycor() + 20;
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20;
    paddle.goto(paddle.xcor(), new_y)


sceen.onkey(go_up, "Up")
sceen.onkey(go_down, "Down")
sceen.exitonclick()
