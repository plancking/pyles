import time,turtle
import random as r

def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for i in [0,60,-120,60]:
            turtle.left(i)
            koch(size/3,n-1)

def drawf(size,n):
    for i in range(3):
        koch(size,n)
        turtle.right(120)

turtle.screensize(800,800)
for i in range(50):
    turtle.pensize(2)
    turtle.color("black")
    turtle.hideturtle()
    x,y,angle=r.randint(-400,400),r.randint(-400,400),r.randint(0,359)
    turtle.penup()
    turtle.goto(x,y)
    turtle.seth(angle)
    turtle.pendown()
    turtle.tracer(0)
    drawf(r.randint(40,200),4)
    turtle.update()
    



