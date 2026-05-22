from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

# Creating snake, food and scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

# Creating controls for the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
delay =  0.1
while is_game_on:
    screen.update()
    time.sleep(delay)

    snake.move()


    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        delay -= 0.005


    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()


    #detect collision with the tail
    for segment in snake.segments[1:]:
        # except the collision with the head itself

        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()