#Exercise 4
#YpolGeom
#Panagiotis Vlassis
#1115201400022

from sympy import Point, Polygon, Circle, Triangle
from matplotlib import path
from random import randint
import numpy as np

n=input("Give number of tests: ")

ax=randint(0,20)
ay=randint(0,20)
bx=randint(0,20)
by=randint(0,20)
cx=randint(0,20)
cy=randint(0,20)
dx=randint(0,20)
dy=randint(0,20)
ex=randint(0,20)
ey=randint(0,20)

print("\nCreate polygon with points (%d,%d),(%d,%d),(%d,%d),(%d,%d),(%d,%d)" %(ax,ay,bx,by,cx,cy,dx,dy,ex,ey))

pol = Polygon( (ax,ay),(bx,by),(cx,cy),(dx,dy),(ex,ey) )

ax=randint(0,20)
ay=randint(0,20)
bx=randint(0,20)
by=randint(0,20)
cx=randint(0,20)
cy=randint(0,20)

print("Create cycle with points (%d,%d),(%d,%d),(%d,%d)" %(ax,ay,bx,by,cx,cy))
c = Circle( (ax,ay),(bx,by),(cx,cy) )

print("\n------------------------------------")
print(">>Polygon test with encloses_point<<")
print("------------------------------------")
for i in range(n):
    xcord=randint(0,10)
    ycord=randint(0,10)
    print("Test if polygon encloses point(%d,%d)" %(xcord,ycord))
    print pol.encloses_point(Point(xcord,ycord))

print("\n-----------------------------")
print(">>Circle test with encloses<<")
print("-----------------------------")
for i in range(n):
    ax=randint(0,20)
    ay=randint(0,20)
    bx=randint(0,20)
    by=randint(0,20)
    cx=randint(0,20)
    cy=randint(0,20)
    t = Triangle((ax,ay),(bx,by),(cx,cy))
    print("Test if circle encloses Triangle with vertices (%d,%d),(%d,%d),(%d,%d)" %(ax,ay,bx,by,cx,cy))
    print c.encloses(t)

print("\n-----------------------------")
print(">>Test for path contains_point<<")
print("-----------------------------")

ax=randint(0,20)
ay=randint(0,20)
bx=randint(0,20)
by=randint(0,20)
cx=randint(0,20)
cy=randint(0,20)
dx=randint(0,20)
dy=randint(0,20)

print("Create path with points (%d,%d),(%d,%d),(%d,%d),(%d,%d)" %(ax,ay,bx,by,cx,cy,dx,dy))
p = path.Path([(ax,ay),(bx,by),(cx,cy),(dx,dy)])

for i in range(n):
    a=randint(0,20)
    b=randint(0,20)
    print("Test point (%d,%d)" %(a,b))
    print p.contains_point(Point(a,b))

print("\n-----------------------------")
print(">>Test for path contains_points<<")
print("-----------------------------")
points=[]

for i in range(n):
    points.append(Point(randint(0,20),randint(0,20)))
print p.contains_points(points)
