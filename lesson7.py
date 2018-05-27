import turtle as t
import time
def drawline(leng):
    t.fd(leng)
    t.right(90)
    t.penup()

def drawnum(num,leng):
    if num in [2,3,4,5,6,8,9]:
        t.pendown() 
    drawline(leng)
    if num in [0,1,3,4,5,6,7,8,9]:
        t.pendown() 
    drawline(leng)
    if num in [0,2,3,5,6,8,9]:
        t.pendown() 
    drawline(leng)
    if num in [0,2,6,8]:
        t.pendown() 
    drawline(leng)
    t.left(90)
    if num in [0,4,5,6,8,9]:
        t.pendown() 
    drawline(leng)
    if num in [0,2,3,5,6,7,8,9]:
        t.pendown() 
    drawline(leng)
    if num in [0,1,2,3,4,7,8,9]:
        t.pendown()
    drawline(leng)
    t.left(180)
    t.penup()
    

t.screensize(800,500)
t.hideturtle()
for i in range(10):
    t.pensize(20)
    t.hideturtle()
    t.penup()
    t.color("red")
    t.tracer(0)
    drawnum(9-i,200)
    t.update()
    time.sleep(1)
    t.reset()

