#Exercise 2
#YpolGeom
#Panagiotis Vlassis
#1115201400022

from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np

n=input('Give number of vertices: ')
points = np.random.rand(n,2)
tri = Delaunay(points)
plt.triplot(points[:,0],points[:,1],tri.simplices)
plt.plot(points[:,0],points[:,1],'o')
plt.show()
