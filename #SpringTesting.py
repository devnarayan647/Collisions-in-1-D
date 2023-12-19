#SpringTesting
from vpython import *
from math import *
ball1=sphere(pos=vector(-5,0,0),radius=0.5,color=color.cyan,make_trail=True)
ball2=sphere(pos=vector(5,0,0),radius=0.5,color=color.cyan,make_trail=True)
wall1=box(pos=vector(-7,0,0),size=vector(0.2,3,3),color=color.green)
wall2=box(pos=vector(7,0,0),size=vector(0.2,3,3),color=color.green)
spring=helix(pos=ball1.pos,axis=ball1.axis,radius=0.5,length=9,coils=15)
ball1.velocity=vector(10,0,0)
ball2.velocity=vector(-10,0,0)
deltat=0.005
t=0
vscale=0.1
trail1=arrow(pos=ball1.pos,axis=vscale*ball1.velocity,color=color.magenta)
trail2=arrow(pos=ball2.pos,axis=vscale*ball2.velocity,color=color.magenta)
ball1.pos=(ball1.pos+(ball1.velocity*deltat))
ball2.pos=(ball2.pos+(ball2.velocity*deltat))
scene.autoscale=False
while True:
    rate(100)
    if abs(ball1.pos.x-ball2.pos.x)<=(ball1.radius*2):
        ball1.velocity.x=-ball1.velocity.x
        ball2.velocity.x=-ball2.velocity.x
       
    if ball1.pos.x<wall1.pos.x+ball1.radius or ball2.pos.x>wall2.pos.x+ball2.radius:
        ball1.velocity.x=-(ball1.velocity.x)    
        ball2.velocity.x=-(ball2.velocity.x)
    trail1.axis=vscale*ball1.velocity
    trail2.axis=vscale*ball2.velocity    
    ball1.pos=ball1.pos+(ball1.velocity*deltat)
    ball2.pos=ball2.pos+(ball2.velocity*deltat)
    trail1.pos=ball1.pos
    trail2.pos=ball2.pos
    t=t+deltat        