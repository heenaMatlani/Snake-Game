from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.set_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.resets()
        snake.reset()
    # for segment in range(len(snake.all_squares)-1):
    #     if segment == 0:
    #         pass
    #     elif snake.head.distance(snake.all_squares[segment]) < 10:
    #         print(segment)
    #         game_is_on = False
    #         scoreboard.game_over()
    for segment in snake.all_squares:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.resets()
            snake.reset()

screen.exitonclick()
