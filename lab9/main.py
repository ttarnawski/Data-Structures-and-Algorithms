from lab9 import AdjacencyList

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.get_vertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(j, w, end=";")
        print()
    print("-------------------")

graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)]

adjacency_list = AdjacencyList()

for edge in graf:
    vertex1, vertex2, distance = edge
    adjacency_list.insert_edge(vertex1, vertex2, distance)

# print(adjacency_list)
# print(adjacency_list.neighbours(0))
# print(adjacency_list.adjacency_list)
printGraph(adjacency_list.prim_algorithm('A'))





