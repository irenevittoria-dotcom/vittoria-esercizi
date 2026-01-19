from turtle import *
import math

title("Isosceles triangle circle")
setup(1000, 1000)
setworldcoordinates(-500, -500, 500, 500)
hideturtle()
tracer(0, 0)

def isoscelestriagle(x, y, width, height, direction, color):
    up()
    goto(x, y)
    seth(direction -90)
    fd(width/2)
    #bottom right corner
    p1x, p1y = xcor(), ycor()
    back(width)
    #bottom left corner
    p2x, p2y = xcor(), ycor()

    goto(x, y)
    seth(direction)
    fd(height)
    # top corner
    p3x, p3y = xcor(), ycor()

    goto(p1x, p1y)
    down()
    fillcolor(color)
    begin_fill()
    goto(p2x, p2y)
    goto(p3x, p3y)
    goto(p1x, p1y)
    end_fill








