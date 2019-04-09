#Exercise 2
#YpolGeom
#Panagiotis Vlassis
#1115201400022

#Input: [r] #radius of circle
#Output: [numOfLatticePoints]

import math

def findNumOfLatticePoints(r):
	num=4
	for x in range(1,r):
		y_2=r*r-x*x
		y=int(math.sqrt(y_2))
		if(y*y==y_2):
			num+=4
	return num

r=input("Give r: ")
print("Number of lattice points: %d" %findNumOfLatticePoints(r))

