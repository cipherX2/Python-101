from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
# tim = Turtle()
# tim.penup()
# tim.shape("turtle")
# tim.goto(x=-230, y=-100)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []


def make_turtles():
    for item in colors:
        tim = Turtle()
        tim.color(item)
        tim.shape("turtle")
        tim.penup()
        turtles.append(tim)
    # print(turtles)


def goto_start():
    x_cor = -230
    y_cor = -100
    for each in turtles:
        each.goto(x=x_cor, y=y_cor)
        y_cor += 40


make_turtles()
goto_start()

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won the turtle bet")
                break
            else:
                print(f"you've lose,{winning_color} is the winner!! lel (:")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
