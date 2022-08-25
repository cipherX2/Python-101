import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.pensize(10)
tim.speed(0)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


directions = [0, 90, 180, 270]

for _ in range(300):
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
