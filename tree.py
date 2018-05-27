import turtle as t
import random as ra
def draw(leng,n):
    if n==0:
        c=["red","blue","green","black","purple","pink","cyan"]
        ra.shuffle(c)
        t.color(c[0])
        t.fd(leng)
        t.left(60)
        t.color(c[1])
        t.fd(leng)
        t.backward(leng)
        t.right(120)
        t.color(c[2])
        t.fd(leng)
        t.backward(leng)
        t.left(60)
        t.color(c[3])
        t.backward(leng)
    else:
        t.fd(leng)
        for angle in [60,-120]:
            t.left(angle)
            draw(0.618*leng,n-1)
        t.left(60)
        t.backward(leng)

t.screensize(800,800)
t.penup()
t.goto(0,-300)
t.seth(90)

t.pensize(2)
t.pendown()
t.tracer(0)
draw(300,10)
t.update()

