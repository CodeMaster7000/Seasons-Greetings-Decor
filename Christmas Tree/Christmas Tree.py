n = 50
from turtle import *
speed("fastest")
left(90)
forward(3*n)
color("dark green")
backward(n*4.8)
def tree(d, s):
    if d <= 0:
        return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.5)
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)
tree(15, n)
backward(n/2)
ht()
