import polska
from lab7 import AdjacencyList
from lab7 import AdjacencyMatrix


def main1():
    adjacency_list = AdjacencyList()

    for rej in polska.slownik.keys():
        adjacency_list.insert_vertex(rej)

    for edge in polska.graf:
        x, y = edge
        adjacency_list.insert_edge(x, y)

    adjacency_list.delete_vertex('K')
    adjacency_list.delete_edge('W', 'E')

    polska.draw_map(adjacency_list.edges())


def main2():
    adjacency_matrix = AdjacencyMatrix()

    for rej in polska.slownik.keys():
        adjacency_matrix.insert_vertex(rej)

    for edge in polska.graf:
        x, y = edge
        adjacency_matrix.insert_edge(x, y)

    adjacency_matrix.delete_vertex('K')
    adjacency_matrix.delete_edge('W', 'E')

    polska.draw_map(adjacency_matrix.edges())


main1()
