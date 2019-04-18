#Exercise 1
#YpolGeom
#Panagiotis Vlassis
#1115201400022

from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np

n=input('Give number of vertices: ')
points = np.random.rand(n,2)
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
