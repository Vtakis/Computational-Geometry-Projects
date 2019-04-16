import numpy as np
from scipy.spatial import cKDTree

n_voronoi, n_test = 10, 10

voronoi_points = np.random.rand(n_voronoi, 2)
test_points = np.random.rand(n_test, 2)

voronoi_kdtree = cKDTree(voronoi_points)

test_point_dist, test_point_regions = voronoi_kdtree.query(test_points, k=1)

print test_point_dist
print test_point_regions
