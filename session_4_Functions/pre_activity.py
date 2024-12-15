#function def
#function Scope
import turtle
t = turtle.Turtle()
t.color("yellow")


def square():
    for x in range(4):
        t.forward(100)
        t.right(90)


square()
for i in range(80):
    square()
    t.forward(5)
    t.left(5)
turtle.done()