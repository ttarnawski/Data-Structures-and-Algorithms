import math


class AdjacencyList:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.adjacency_list = []

    def insert_vertex(self, vertex):
        self.list.append(Vertex(vertex))
        self.adjacency_list.append([])
        self.dict[vertex] = self.get_vertex_idx(vertex)

    def insert_edge(self, vertex1, vertex2, edge):
        if vertex1 not in self.list:
            self.insert_vertex(vertex1)
        if vertex2 not in self.list:
            self.insert_vertex(vertex2)
        # if vertex2 not in self.adjacency_list[self.dict[vertex1]]:
        self.adjacency_list[self.dict[vertex1]].append((vertex2, Edge(edge)))
        # if vertex1 not in self.adjacency_list[self.dict[vertex2]]:
        self.adjacency_list[self.dict[vertex2]].append((vertex1, Edge(edge, True)))

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
            neighbours.append(neighbour)
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

    def bfs(self, s='s'):
        visited = []
        parent = [-1 for _ in range(self.order())]
        queue = [self.get_vertex_idx(s)]
        visited.append(self.get_vertex_idx(s))
        while queue:
            current_vertex = queue.pop(0)
            neighbours = self.neighbours(current_vertex)
            for neighbour in neighbours:
                if self.get_vertex_idx(neighbour[0]) not in visited and neighbour[1].residual > 0:
                    queue.append(self.get_vertex_idx(neighbour[0]))
                    visited.append(self.get_vertex_idx(neighbour[0]))
                    parent[self.get_vertex_idx(neighbour[0])] = current_vertex
        return parent

    def path_analysis(self, parent, s='s', t='t'):
        current_index = self.get_vertex_idx(t)
        min_capacity = math.inf
        if parent[current_index] >= 0:
            while current_index != self.get_vertex_idx(s):
                neighbours = self.neighbours(parent[current_index])
                for neighbour in neighbours:
                    if self.get_vertex_idx(neighbour[0]) == current_index and neighbour[1].isResidual is False:
                        if neighbour[1].residual < min_capacity:
                            min_capacity = neighbour[1].residual
                        break
                current_index = parent[current_index]
            return min_capacity
        else:
            return 0

    def path_augmentation(self, parent, min_capacity, s='s', t='t'):
        current_index = self.get_vertex_idx(t)
        if parent[current_index] >= 0:
            while current_index != self.get_vertex_idx(s):
                neighbours = self.neighbours(parent[current_index])
                for neighbour in neighbours:
                    if self.get_vertex_idx(neighbour[0]) == current_index:
                        if neighbour[1].isResidual is False:
                            neighbour[1].flow += min_capacity
                            neighbour[1].residual -= min_capacity
                        if neighbour[1].isResidual is True:
                            neighbour[1].residual += min_capacity
                        break
                current_index = parent[current_index]

    def ford_fulkerson(self):
        parent = self.bfs()
        min_capacity = self.path_analysis(parent)
        while min_capacity > 0:
            self.path_augmentation(parent, min_capacity)
            parent = self.bfs()
            min_capacity = self.path_analysis(parent)

        flow_sum = 0
        for edge in self.adjacency_list[self.get_vertex_idx('t')]:
            vertex = edge[0][0]
            for edge2 in self.adjacency_list[self.get_vertex_idx(vertex)]:
                if edge2[0][0] == 't':
                    flow_sum += edge2[1].flow
        return flow_sum


class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other

    def __str__(self):
        return str(self.key)


class Edge:
    def __init__(self, capacity, isResidual=False):
        self.capacity = capacity
        self.flow = 0
        if isResidual is False:
            self.residual = capacity
        else:
            self.residual = 0
        self.isResidual = isResidual

    def __repr__(self):
        return str(self.capacity) + ' ' + str(self.flow) + ' ' + str(self.residual) + ' ' + str(self.isResidual)
