
from random import randint

from turtle import forward, speed, left, penup, pendown, exitonclick

speed("slow")

infl = 40

def slupek(a,b):
    for _ in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)

for _ in range (15):
    slupek(20,infl)
    penup()
    forward(40)
    pendown()
    infl += randint (-20, 55)

exitonclick()
