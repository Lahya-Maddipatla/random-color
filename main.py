from turtle import *
import random
t=Turtle()
colormode(255)
directions=[0,270,180,90]
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
for i in range(200):
    t.pensize(5)
    t.forward(30)
    t.setheading(random.choice(directions))
    t.color(random_color())
s=Screen()
s.exitonclick()