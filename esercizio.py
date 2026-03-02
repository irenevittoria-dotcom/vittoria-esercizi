import turtle
import random

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title("Typing Game")
screen.bgcolor("blue")
turtle.hideturtle


turtle.up()
turtle.color("red")
scoreturd = turtle.Turtle()
scoreturd.color("red")
scoreturd.hideturd()
scoreturd.up()
turtle.goto(350, 400)
turtle.write("Score: ", align='center', font=('Courler', 25,'normal'))

minspeed= 5
maxspeed= 30
letters= []
speed= []
pos= []
lts= []
n = 10
gameover = False
score= 0

def increase_difficulty():
    global minspeed, maxspeed
    minspeed += 1
    maxspeed += 1
    screen.ontimer(increase_difficulty, 5000)

def drawgameover():
    turtle.goto(0, 0)
    turtle.color('red')
    turtle.write('GAME OVER', 'center', font=('Courler'))
    turtle.goto(0, -150)
    turtle.color("orange")
    turtle.write('Your score is ()')
