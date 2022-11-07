import turtle as t
import random
turtle = t.Turtle()

t.colormode(255)

turtle.speed(10)
turtle.pensize(5)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range (200):

    turtle.color(random_color())    
    turtle.forward(30)
    turtle.setheading(random.choice(directions))



