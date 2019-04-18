#Exercise 3
#YpolGeom
#Panagiotis Vlassis
#1115201400022

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
from random import randint

n=input('Give number of vertices: ')

row=[]
col=[]
weight=[]

#create edges with weight
for i in range(n):
    row.append(randint(0,n))
    col.append(randint(0,n))
    weight.append(randint(0,2*n))

#create graph
graph=csr_matrix((weight,(row,col)),shape=(n+1,n+1))
print graph

#create distance matrix
dist_matrix,predecessors = shortest_path(graph,method='D',return_predecessors=True)
print("\ndistance matrix")
print dist_matrix
print("\nPredecessors matrix -> find shortest path from point i")
print predecessors
