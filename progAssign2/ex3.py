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
graph=csr_matrix((weight,(row,col)),shape=(n+2,n+2))
print graph

#create distance matrix
dist_matrix, predecessors = shortest_path(graph,method='FW',return_predecessors=True)
print dist_matrix
