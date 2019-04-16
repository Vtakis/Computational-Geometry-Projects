from sympy import Point, Polygon, Circle, Triangle
from matplotlib import path
from random import randint
import numpy as np

n=input("Give number of tests: ")

pol = Polygon( (randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)) )

c = Circle( (randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)) )

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
p = path.Path([(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20))])
print p.contains_point(Point(randint(0,20),randint(0,20)))

print("\n-----------------------------")
print(">>Test for path contains_points<<")
print("-----------------------------")
p = path.Path([(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20)),(randint(0,20),randint(0,20))])
points=[]

for i in range(10):
    points.append(Point(randint(0,20),randint(0,20)))
print p.contains_points(points)
