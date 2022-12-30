from random import randint
from processing import *
numberOfParticules = 40;
position=[]
velocity=[]
lifespan=[]
color=1
def setup():
    size(300,300)
    frameRate(24)  
    background(0) 
    stroke(255)
    strokeWeight(2)
    global numberOfParticules
    global position
    global velocity
    global lifespan
    for i in range(0, numberOfParticules):
        position.append([0,0])
        if (i < numberOfParticules/2):
            velocity.append([randint(-2,2), randint(-10,-5)])
            lifespan.append(randint(20,40))
        else: 
            velocity.append([0,0])
            lifespan.append(randint(0,40))
