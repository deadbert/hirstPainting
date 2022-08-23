# import colorgram
#
# extracted_colors = colorgram.extract('image.jpg', 30)
# color_list = []
#
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_list.append(rgb)
#
# print(color_list)

# 10 x 10 grid of dots
# dots 20 in size
# spaced 50 appart

from turtle import Turtle, Screen
import random

bob = Turtle()
bob.hideturtle()
bob.penup()
bob.speed('fastest')

screen = Screen()
screen.colormode(255)

final_colors = [(34, 108, 167), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27),
                (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97),
                (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143),
                (111, 41, 49), (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45),
                (35, 55, 46), (99, 93, 2)
                ]


def print_line(painter, colors):
    for _ in range(num_x_dots):
        painter.dot(20, random.choice(colors))
        painter.forward(50)


num_x_dots = 10
num_y_dots = 10
x_start = -250
y_start = -250
bob.setposition(x_start, y_start)
for _ in range(num_y_dots):
    print_line(bob, final_colors)
    location = bob.position()
    y = location[1]
    bob.setposition(x_start, y + 50)


screen.exitonclick()
