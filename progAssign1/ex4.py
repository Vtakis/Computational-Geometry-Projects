#Exercise 4
#YpolGeom
#Panagiotis Vlassis
#1115201400022

#Input: set of points in plane
#Output: set of points for convex hull

from random import randint

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def orientation(a,b,c):
	val=(b.y-a.y)*(c.x-b.x)-(b.x-a.x)*(c.y-b.y)
	if(val==0):
		return 0
	elif(val>0):
		return 1
	else:
		return 2

def convexHull(points,n):
	next=[]
	for i in range(n):
		next.append(-1)
	left=0;
	for i in range(1,n):
		if(points[i].x<points[left].x):
			left=i
	p=left
	while True:
		q=(p+1)%n
		for i in range(n):
			if(orientation(points[p],points[i],points[q])==2):
				q=i
		next[p]=q
		p=q
		if(p==left):
			break
	for i in range(n):
		if(next[i]!=-1):
			print("(%d,%d)" %(points[i].x,points[i].y))

n=input("Give 'n' (number of points): ")
if(n<3):
	print('Give n>=3!')
else:
	points=[]
	for i in range(n):
		points.append(Point(randint(0,10000),randint(0,10000)))
	print('Points of convex hull')
	convexHull(points,n)
