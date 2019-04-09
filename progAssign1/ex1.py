#Exercise 1
#YpolGeom
#Panagiotis Vlassis
#1115201400022

#Input: [A,B,C] in form of (x,y)
#Output: print message


def areaCalc(xA, yA, xB, yB, xC, yC):  
    return abs((xA * (yB - yC) + xB * (yC - yA)+ xC * (yA - yB)) / 2.0)

def checkZeroPointInTriangle(xA,yA,xB,yB,xC,yC):
	A1=areaCalc(0,0,xB,yB,xC,yC)
	A2=areaCalc(xA,yA,0,0,xC,yC)
	A3=areaCalc(xA,yA,xB,yB,0,0)

	A=areaCalc(0,0,xB,yB,xC,yC)

	if(A==A1+A2+A3):
		print('(0,0) inside in given triangle')
	else:
		print('(0,0) NOT inside in given triangle')

print('Enter (x,y) for points A,B,C')
xA=input("xA: ")
yA=input("yA: ")
xB=input("xB: ")
yB=input("yB: ")
xC=input("xC: ")
yC=input("yC: ")

checkZeroPointInTriangle(xA,yA,xB,yB,xC,yC)
