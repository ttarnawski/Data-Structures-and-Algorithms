#!/usr/bin/python
# -*- coding: utf-8 -*-

class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other

    def __str__(self):
        return str(self.key)


class AdjacencyList:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.adjacency_list = []

    def insert_vertex(self, vertex):
        self.list.append(Vertex(vertex))
        self.adjacency_list.append([])
        self.dict[vertex] = self.get_vertex_idx(vertex)

    def insert_edge(self, vertex1, vertex2, edge=0):
        if vertex2 not in self.adjacency_list[self.dict[vertex1]]:
            self.adjacency_list[self.dict[vertex1]].append(vertex2)
        if vertex1 not in self.adjacency_list[self.dict[vertex2]]:
            self.adjacency_list[self.dict[vertex2]].append(vertex1)

    def delete_vertex(self, vertex):
        del self.adjacency_list[self.get_vertex_idx(vertex)]
        del self.list[self.get_vertex_idx(vertex)]
        del self.dict[vertex]
        for key in self.dict.keys():
            self.dict[key] = self.get_vertex_idx(key)
        for neighbours in self.adjacency_list:
            for neighbour in neighbours:
                if neighbour == vertex:
                    neighbours.remove(vertex)

    def delete_edge(self, vertex1, vertex2):
        self.adjacency_list[self.get_vertex_idx(vertex1)].remove(vertex2)
        self.adjacency_list[self.get_vertex_idx(vertex2)].remove(vertex1)

    def get_vertex_idx(self, vertex):
        return self.list.index(vertex)

    def get_vertex(self, vertex_idx):
        return self.list[vertex_idx]

    def neighbours(self, vertex_idx):
        neighbours = []
        for neighbour in self.adjacency_list[vertex_idx]:
            neighbours.append(self.get_vertex_idx(neighbour))
        return neighbours

    def order(self):
        return len(self.list)

    def size(self):
        # krawędź z A do B oraz B do A liczę jako 1
        size = 0
        for neighbours in self.adjacency_list:
            size += len(neighbours)
        return int(size / 2)

    def edges(self):
        edges = []
        index = 0
        for vertex in self.list:
            for neighbour in self.adjacency_list[index]:
                edges.append((vertex.key, neighbour))
            index += 1
        return edges

    def __str__(self):
        string = ''
        for vertex in self.list:
            string += str(vertex) + ' '
        return string

    def test(self):
        string = ''
        for vertex, index in self.dict.items():
            string += str(vertex) + ' -> ' + str(index) + ' '
        return string

    def test2(self):
        string = ''
        for vertex in self.adjacency_list:
            string += '['
            for edges in vertex:
                string += str(edges)
            string += '] '
        return string


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
