from turtle import *
from shapes import *
from random import randint

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#69D9FF")

y = -100
width = 240

draw_rectangle(myPen, "brown", -15, y-40, 30, 40)

while width>20:
  width = width - randint(20,30)
  height = randint(15,35)
  x = 0 - width/2
  draw_rectangle(myPen, "green", x, y, width, height)
  y = y + height
  
draw_star(myPen, "yellow", 4, y, 20)

myPen.penup()
myPen.color("red")
myPen.goto(-100, -180)
myPen.write("Merry Christmas!", None, None, "24pt bold")
myPen.hideturtle()  
