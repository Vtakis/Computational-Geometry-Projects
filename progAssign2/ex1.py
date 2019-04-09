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

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Voronoi.html#scipy.spatial.Voronoi
#https://puckey.studio/projects/delaunay-raster
#https://www.slideshare.net/AdritaChakraborty/delaunay-triangulation
#https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&ved=2ahUKEwjXv8LjnMDhAhXKk4sKHRepBTAQFjAFegQIAhAC&url=http%3A%2F%2Fdccg.upc.edu%2Fpeople%2Fvera%2Fwp-content%2Fuploads%2F2013%2F06%2FTerrains.ppt&usg=AOvVaw1_bFrbBOMIiED8fMpWK2oY
#https://slideplayer.com/slide/3313364/
#https://en.wikibooks.org/wiki/Trigonometry/For_Enthusiasts/Delaunay_triangulation
#www.cse.ust.hk/~scheng/book/Delmesh/chapter2.pdf
