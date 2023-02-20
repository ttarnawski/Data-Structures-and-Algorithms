from copy import deepcopy
import numpy as np


class AdjacencyMatrix:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.adjacency_matrix = []

    def insert_vertex(self, vertex):
        self.list.append(Vertex(vertex))
        self.adjacency_matrix.append([0])
        self.dict[vertex] = self.get_vertex_idx(vertex)
        for i in range(len(self.list)):
            self.adjacency_matrix[i] = [0 for vertex in self.list]

    def insert_edge(self, vertex1, vertex2, edge=1):
        if vertex1 not in self.list:
            self.insert_vertex(vertex1)
        if vertex2 not in self.list:
            self.insert_vertex(vertex2)
        self.adjacency_matrix[self.dict[vertex1]][self.dict[vertex2]] = edge
        self.adjacency_matrix[self.dict[vertex2]][self.dict[vertex1]] = edge

    def delete_vertex(self, vertex):
        del self.adjacency_matrix[self.get_vertex_idx(vertex)]
        for row in range(len(self.adjacency_matrix)):
            del self.adjacency_matrix[row][self.get_vertex_idx(vertex)]
        del self.list[self.get_vertex_idx(vertex)]
        del self.dict[vertex]
        for key in self.dict.keys():
            self.dict[key] = self.get_vertex_idx(key)

    def delete_edge(self, vertex1, vertex2):
        self.adjacency_matrix[self.get_vertex_idx(vertex1)][self.get_vertex_idx(vertex2)] = 0
        self.adjacency_matrix[self.get_vertex_idx(vertex2)][self.get_vertex_idx(vertex1)] = 0

    def get_vertex_idx(self, vertex):
        return self.list.index(vertex)

    def get_vertex(self, vertex_idx):
        return self.list[vertex_idx]

    def neighbours(self, vertex_idx):
        neighbours = []
        for edge in range(len(self.adjacency_matrix[vertex_idx])):
            if self.adjacency_matrix[vertex_idx][edge] != 0:
                neighbours.append(edge)
        return neighbours

    def order(self):
        return len(self.list)

    def size(self):
        # krawędź z A do B oraz B do A liczę jako 1
        size = 0
        for vertex in self.adjacency_matrix:
            for edge in vertex:
                if edge != 0:
                    size += 1
        return int(size / 2)

    def edges(self):
        edges = []
        index = 0
        for vertex in self.list:
            for edge in range(len(self.adjacency_matrix[index])):
                if self.adjacency_matrix[index][edge] != 0:
                    edges.append((vertex.key, self.list[edge].key))
            index += 1
        return edges


class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other


def ullman(G, P, M):
    def ullman_(G, P, M, used_columns=[], current_row=0, result=[], no_recursion=0):
        no_recursion += 1
        if current_row == M.shape[0]:
            if np.array_equal(M @ np.transpose((M @ np.array(G.adjacency_matrix))), np.array(P.adjacency_matrix)):
                return no_recursion, M
            else:
                return no_recursion

        M_prim = deepcopy(M)

        # M0
        # M_0 = deepcopy(M)
        # for i in range(M_0.shape[0]):
        #     for j in range(M_0.shape[1]):
        #         if len(P.neighbours(i)) <= len(G.neighbours(j)):
        #             M_0[i][j] = 1
        #         else:
        #             M_0[i][j] = 0

        # pruning
        # M_pruning = deepcopy(M)
        # was_changed = True
        # while was_changed is True:
        #     was_changed = False
        #     for i in range(M.shape[0]):
        #         for j in range(M.shape[1]):
        #             if M_pruning[i][j] == 1:
        #                 p_neighbours = P.neighbours(i)
        #                 g_neighbours = G.neighbours(j)
        #                 if len(p_neighbours) == len(g_neighbours):
        #                     mapped_p = []
        #                     mapped_g = []
        #                     for p_neighbour in p_neighbours:
        #                         for g_neighbour in g_neighbours:
        #                             if M_pruning[p_neighbour][g_neighbour] == 1 and p_neighbour not in mapped_p and g_neighbour not in mapped_g:
        #                                 mapped_p.append(p_neighbour)
        #                                 mapped_g.append(g_neighbour)
        #                     if len(mapped_p) != len(p_neighbours):
        #                         M_pruning[i][j] = 0
        #                         was_changed = True

        for column in range(M.shape[1]):
            if column not in used_columns:
                for i in range(M.shape[1]):
                    if i == column:
                        M_prim[current_row][i] = 1
                    else:
                        M_prim[current_row][i] = 0
                # M0
                # if M_0[current_row][column] == 0:
                #     continue

                # pruning
                # if M_pruning[current_row][column] == 0:
                #     continue

                used_columns.append(column)
                no_recursion = ullman_(G, P, M_prim, used_columns, current_row + 1, result, no_recursion)
                if isinstance(no_recursion, tuple):
                    result.append(no_recursion[1])
                    no_recursion = no_recursion[0]
                used_columns.remove(column)
        return no_recursion

    result = []
    no_recursion = ullman_(G, P, M, result=result)
    return len(result), no_recursion


def prune(G, P, M):
    was_changed = True
    while was_changed is True:
        was_changed = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i][j] == 1:
                    p_neighbours = P.neighbours(i)
                    g_neighbours = G.neighbours(j)
                    if len(p_neighbours) == len(g_neighbours):
                        mapped_p = []
                        mapped_g = []
                        for p_neighbour in p_neighbours:
                            for g_neighbour in g_neighbours:
                                if M[p_neighbour][g_neighbour] == 1 and p_neighbour not in mapped_p and g_neighbour not in mapped_g:
                                    mapped_p.append(p_neighbour)
                                    mapped_g.append(g_neighbour)
                        if len(mapped_p) != len(p_neighbours):
                            M[i][j] = 0
                            was_changed = True
    return M

