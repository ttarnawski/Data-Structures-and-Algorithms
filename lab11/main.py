from lab11 import AdjacencyMatrix
from lab11 import ullman
import numpy as np

graph_G_vertexes = ['A', 'B', 'C', 'D', 'E', 'F']
graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]

graph_P_vertexes = ['A', 'B', 'C']
graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

G = AdjacencyMatrix()
P = AdjacencyMatrix()

for vertex in graph_G_vertexes:
    G.insert_vertex(vertex)

for edge in graph_G:
    vertex1, vertex2, edge1 = edge
    G.insert_edge(vertex1, vertex2, edge1)

for vertex in graph_P_vertexes:
    P.insert_vertex(vertex)

for edge in graph_P:
    vertex1, vertex2, edge1 = edge
    P.insert_edge(vertex1, vertex2, edge1)

M = np.zeros((P.order(), G.order()))

print(ullman(G, P, M))

# t1 = 2, 5, 6
# t2 = t1[0] + 1, t1[1], t1[2]
# print(t1)
# print(t2)