from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.pensize(3)

def move_forwards():
    tim.forward(15)
    pass

def move_backwards():
    tim.backward(15)
    pass

def turn_left():
    tim.setheading(tim.heading() + 15) ## or .left(15)
    pass

def turn_right():
    tim.setheading(tim.heading() - 15) ## or .right(15)
    pass

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    pass

screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")



screen.exitonclick()