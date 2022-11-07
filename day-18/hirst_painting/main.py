from extracting_colors import color_list
import turtle as t
import random
turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)
turtle.speed("fastest")

turtle.penup()
turtle.hideturtle()

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)


number_of_dots = 100
for dot_count in range (1, number_of_dots + 1):
    
    turtle.dot(30, random.choice(color_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)



screen.exitonclick()
 
