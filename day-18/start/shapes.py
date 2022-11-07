from turtle import Turtle
import random
turtle = Turtle()
turtle.pensize(5)
colors = ["WhiteSmoke", "SpringGreen", "DeepPink", "MediumSlateBlue", "Tomato", "Gold", "Cyan", "Blue", "LemonChiffon"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range (num_sides):
        turtle.forward(100)
        turtle.right(angle)
        
    
    
for i in range (3, 11):
    turtle.color(random.choice(colors))
    draw_shape(i)