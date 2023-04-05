import random
import turtle
from turtle import Turtle, Screen

colors_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
color= random.choice(colors_list)
timmy = Turtle()

# turtle.setworldcoordinates(-200, -200, 200, 200)


start_pos = (-200, 0)
timmy.penup()
timmy.goto(start_pos)
# timmy.dot(20,"red")

# Move the turtle in parallel lines
for h in range(5):
    for i in range(5):   # repeat 5 times to draw 5 lines
        for j in range(4):  # repeat 4 times to draw a square
            timmy.dot(20,"red")   # Move the turtle forward 50 pixels
            timmy.right(90)      # Turn the turtle left by 90 degrees
        timmy.dot(20,"red")         # Lift the turtle's pen up
        timmy.goto(start_pos[0] + 60 * (i+1), start_pos[1]) # Move the turtle to a new starting position
        timmy.dot(20,"red")
    start_pos = (-100, 0)
    timmy.goto(start_pos[0] + 60 * (i+1), start_pos[1])
screen = Screen()
screen.exitonclick()