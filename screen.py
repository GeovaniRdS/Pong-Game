from turtle import Screen

class screen_setup():
    new_screen = Screen()
    
    new_screen.bgcolor("black")
    new_screen.setup(width=1100, height=600)

    new_screen.exitonclick()
