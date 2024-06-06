import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)

dun = Turtle()


def random_color():
     r = random.randint(0,255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     colour = (r,g,b)
     return colour


dun.speed(0)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        dun.color(random_color())
        dun.circle(150)
        dun.setheading(dun.heading() + size_of_gap)
draw_spirograph(6)

screen = Screen()
screen.screensize(500,500)
screen.exitonclick()