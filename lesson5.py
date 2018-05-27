import time,turtle

turtle.screensize(800,800)
turtle.hideturtle()
while True:
    time_str=time.ctime()
    turtle.write(time_str)
    sleep(1)
    turtle.clear()
    
