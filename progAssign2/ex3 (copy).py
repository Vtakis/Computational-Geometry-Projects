from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from random import randint
import numpy as np

n=input('Give number of vertices: ')
points = np.random.rand(n,2)
tri = Delaunay(points)
x=points[tri.simplices]
print(x)
print(x[:2])

#r = np.ptp(a,axis=1)

plt.triplot(points[:,0],points[:,1],tri.simplices)
plt.plot(points[:,0],points[:,1],'o')
plt.show()
