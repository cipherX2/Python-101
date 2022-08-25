from turtle import Turtle, Screen
import snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# turtle dimensions: 20x20

segments = []

# My code:

# i = 0
# for _ in range(3):
#     new_turtle = Turtle()
#     new_turtle.shape("square")
#     new_turtle.color("white")
#     new_turtle.home()
#     new_turtle.penup()
#     new_turtle.setx(i)
#     all_turtles.append(new_turtle)
#     i -= 20

snake = snake.Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
            snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
