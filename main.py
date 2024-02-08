from turtle import Turtle, Screen

# Screnn
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")




paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() +20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")

screen.exitonclick()
