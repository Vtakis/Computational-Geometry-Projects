from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from random import randint


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

num=input('Give number of vertices')

points=[]
for i in range(n):
	points.append(Point(randint(0,10000),randint(0,10000)))

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html#scipy.spatial.Delaunay
