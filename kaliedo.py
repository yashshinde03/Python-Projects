import turtle as t
import time as t1

def circle(color,size,angle):
    t.pencolor(color)
    t.circle(size)
    t.right(angle)
    circle(color,size,angle)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle('red',20,40)

t1.sleep(20)
# t.hideturtle()It will pause the screen
