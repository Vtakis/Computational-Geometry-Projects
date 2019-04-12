from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from random import randint
import numpy as np

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

n=input('Give number of vertices: ')

#points=[]

points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
                   [2, 0], [2, 1], [2, 2]])
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
#for i in range(n):
#	points.append(Point(randint(0,10000),randint(0,10000)))
