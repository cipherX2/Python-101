# import colorgram
#
# extracted_values = []
# colors = colorgram.extract("img.jpg", 10)
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     color = (r, g, b)
#     extracted_values.append(color)
#
# print(extracted_values)

color_list = [(253, 251, 34), (25, 249, 25), (152, 251, 21), (197, 13, 32), (249, 237, 21),
              (40, 76, 188), (39, 216, 69), (238, 227, 5), (228, 160, 48), (244, 247, 253)]

# 10 x 10 rows
import turtle
import random
tim = turtle.Turtle()
turtle.colormode(255)
i = 50

tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for _ in range(10):
    current_position = tim.position()
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setx(current_position[0])
    tim.sety(tim.position()[1]+i)

screen = turtle.Screen()
screen.exitonclick()
