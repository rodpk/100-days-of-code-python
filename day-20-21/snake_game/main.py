from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("=== Snake ===")
screen.tracer(0)  # disable animations


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.035)

    snake.move()
    
    ## detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    ## detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False
        
    ## detect collision with tail
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail
    
    

screen.exitonclick()
