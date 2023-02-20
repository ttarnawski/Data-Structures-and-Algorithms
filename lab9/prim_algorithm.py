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

    def insert_edge(self, vertex1, vertex2, edge=1):
        if vertex1 not in self.list:
            self.insert_vertex(vertex1)
        if vertex2 not in self.list:
            self.insert_vertex(vertex2)
        if vertex2 not in self.adjacency_list[self.dict[vertex1]]:
            self.adjacency_list[self.dict[vertex1]].append((vertex2, edge))
        if vertex1 not in self.adjacency_list[self.dict[vertex2]]:
            self.adjacency_list[self.dict[vertex2]].append((vertex1, edge))

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

    def prim_algorithm(self, s):
        mst = AdjacencyList()
        intree = [0 for n in range(len(self.list))]
        distance = [math.inf for n in range(len(self.list))]
        parents = [-1 for n in range(len(self.list))]

        for vertex in self.list:
            mst.insert_vertex(vertex)

        v = self.get_vertex_idx(s)
        while intree[v] == 0:
            intree[v] = 1
            for neighbour in self.neighbours(v):
                if neighbour[1] < distance[self.get_vertex_idx(neighbour[0])] and neighbour[0] != s and intree[self.get_vertex_idx(neighbour[0])] == 0:
                    distance[self.get_vertex_idx(neighbour[0])] = neighbour[1]
                    parents[self.get_vertex_idx(neighbour[0])] = self.get_vertex(v)

            min_dist = math.inf
            for i in range(len(intree)):
                if intree[i] == 0 and distance[i] < min_dist:
                    min_dist = distance[i]
                    v = i

        sum_distance = 0
        for edge in distance:
            if edge != math.inf:
                sum_distance += edge

        for i in range(len(parents)):
            if i != self.get_vertex_idx(s):
                mst.insert_edge(self.get_vertex(i), parents[i], distance[i])

        return mst


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
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return str(self.distance)
