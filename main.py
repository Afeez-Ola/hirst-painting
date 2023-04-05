import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
start_pos = (0, 0)
timmy.penup()
timmy.goto(start_pos)
timmy.speed("fastest")

colors_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
               (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
               (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
               (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
               (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
hex_color_list = []
hex_color = ""
for i in range(0,len(colors_list)):
    index = random.randint(0, len(colors_list)-1)
    color = colors_list[index]
    # print(color)
    hex_color = "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
    hex_color_list.append(hex_color)


for h in range(6):
    start_pos = (0, 50 * h)
    for i in range(5):
        color_position = random.randint(0, len(hex_color_list))
        for j in range(5):
            print(hex_color_list[color_position])
            timmy.dot(20, hex_color_list[color_position])
            timmy.right(90)
        timmy.goto(start_pos[0] + 60 * i, start_pos[1])  # Move the turtle to a new starting position
        timmy.dot(20, hex_color_list[color_position])

screen = Screen()
screen.exitonclick()
