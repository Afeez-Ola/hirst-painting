# import random
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# start_pos = (-300, -200)
# timmy.penup()
# timmy.goto(start_pos)
# timmy.speed("fastest")
#
# colors_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
#                (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
#                (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
#                (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
#                (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
#
# hex_color_list = []
# for i in range(0,len(colors_list)):
#     index = random.randint(0, len(colors_list)-1)
#     color = colors_list[index]
#     hex_color = "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
#     hex_color_list.append(hex_color)
#
#
# for h in range(10):
#     start_pos = (-300, -200+(50 * h))
#     for i in range(10):
#         color_position = random.randint(0, len(hex_color_list)-1)
#         timmy.dot(20, hex_color_list[color_position])
#         timmy.right(90)
#         timmy.goto(start_pos[0] + 60 * i, start_pos[1])  # Move the turtle to a new starting position
#         timmy.dot(20, hex_color_list[color_position])
#
# screen = Screen()
# screen.exitonclick()

import random
from turtle import Turtle, Screen

# Define constants
START_POS = (-300, -200)
DOT_SIZE = 20
DOT_SPACING = 60
NUM_ROWS = 10
NUM_COLS = 10

# Define colors
COLORS = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
          (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
          (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
          (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
          (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

# Convert colors to hex format
HEX_COLORS = ["#{:02x}{:02x}{:02x}".format(*color) for color in COLORS]

# Set up turtle
timmy = Turtle()
timmy.speed("fastest")
timmy.penup()

# Draw dots
for row in range(NUM_ROWS):
    timmy.hideturtle()
    start_pos = (START_POS[0], START_POS[1] + (50 * row))
    for col in range(NUM_COLS):
        color_index = random.randint(0, len(HEX_COLORS)-1)
        color = HEX_COLORS[color_index]
        timmy.goto(start_pos[0] + (DOT_SPACING * col), start_pos[1])
        timmy.dot(DOT_SIZE, color)

# Set up screen
screen = Screen()
screen.exitonclick()

