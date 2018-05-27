from turtle import *

def koch(size,n):
    if n==0:
        fd(size)
    else:
        for i in [0,60,-120,60]:
            left(i)
            koch(size/3,n-1)


screensize(500,500)
tracer(0)
penup()
goto(-100,100)
pendown()
hideturtle()
color("red")
for i in range(3):
    koch(300,3)
    right(120)
update()

exitonclick()
