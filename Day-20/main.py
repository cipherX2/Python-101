from turtle import Turtle, Screen
import snake
import time

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


screen.exitonclick()
