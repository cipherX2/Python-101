from turtle import Turtle, Screen
from random import choice

colors = ["red", "green", "blue", "black", "pink", "coral", "yellow", "violet", "grey"]
shapes = [
    {"triangle": 3},
    {"square": 4},
    {"pentagon": 5},
    {"hexagon": 6},
    {"heptagon": 7},
    {"octagon": 8},
    {"nonagon": 9},
    {"decagon": 10},
]
tim = Turtle()

for item in shapes:
    for shape in item:
        i = item[shape]
        color = choice(colors)
        angle = 360 / i
        for _ in range(i):
            tim.color(color)
            tim.forward(100)
            tim.right(angle)

screen = Screen()
screen.exitonclick()
