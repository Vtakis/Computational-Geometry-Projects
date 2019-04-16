from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from random import randint
import numpy as np

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

n=input('Give number of vertices: ')
points = np.random.rand(n,2)
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
