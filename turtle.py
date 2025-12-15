import turtle

screen = turtle.Screen()
screen.setup(width=400, height=300)
screen.title("Art")

turtle_start= turtle.Turtle()
turtle_start.speed(1)

screen.colormode(255)

R= 255
G= 182
P= 193
screen.bgcolor((R, G, P))

turtle_start.turtlesize(10)

turtle_start.goto(-100, -100)

turtle_start.begin_fill()
turtle_start.color("red")
turtle_start.forward(3)
turtle_start.right(90)
turtle_start.forward(3)
turtle_start.right(90)
turtle_start.forward(3)

turtle.end_fill


