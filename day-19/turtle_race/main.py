from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle wil win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

turtles = []

y_position = -70
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    
    turtle.goto(x = -230, y = y_position)
    y_position += 30
    
    turtles.append(turtle)
    

print(turtles)


if user_bet: 
    is_race_on = True
    

while is_race_on:
    
    
    for turtle in turtles:
        
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else: 
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)
        
screen.exitonclick()