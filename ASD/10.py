import numpy as np


class Vertex:
    def __init__(self, data):
        self.key = data

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, capacity, is_residual=False):
        self.capacity = capacity
        self.is_residual = is_residual
        self.residual = capacity
        self.flow = 0

    def __str__(self):
        return str(self.capacity) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.is_residual)


class GraphMatrix:
    def __init__(self):
        self.v_list = []
        self.dicto = {}
        self.graph = {}
        self.ssize = 0

    def get_vertex_idx(self, vertex):
        return self.dicto[vertex]

    def get_vertex(self, vertex_idx):
        for key, value in self.dicto.items():
            if value == vertex_idx:
                return key

    def insert_vertex(self, vertex: Vertex):
        self.v_list.append(vertex)
        self.dicto[vertex] = len(self.v_list) - 1
        self.graph[vertex] = {}

    def insert_edge(self, v1, v2, edge: Edge):
        if v1 not in self.v_list:
            self.insert_vertex(v1)
        if v2 not in self.v_list:
            self.insert_vertex(v2)
        self.graph[v1][v2] = edge
        self.ssize += 1

    def delete_edge(self, v1, v2):
        self.graph[v1].pop(v2)
        self.ssize -= 1

    def upgrade_dict(self):
        for i in range(len(self.v_list)):
            self.dicto[self.v_list[i]] = i

    def delete_vertex(self, vertex):
        idx = self.get_vertex_idx(vertex)
        self.v_list.remove(vertex)
        self.dicto.pop(vertex)
        self.upgrade_dict()
        self.graph.pop(vertex)
        for v in self.graph:
            if vertex in self.graph[v]:
                self.graph[v].pop(vertex)

    def neighbours(self, v):
        return self.graph[v].items()

    def size(self):
        return self.ssize

    def order(self):
        return len(self.graph)

    def edges(self):
        result_list = []
        for v1 in self.graph:
            for v2, edge in self.graph[v1].items():
                if v2 < v1:
                    result_list.append((v1.key, v2.key))
        return result_list

    def bfs(self, s):
        visited = {s: None}
        unvisited = [s]
        while unvisited:
            v = unvisited.pop(0)
            for el, w in self.neighbours(v):
                if el not in visited.keys() and w.residual > 0:
                    unvisited.append(el)
                    visited[el] = v
        return visited

    def analiz(self, s, k, parent_list):
        v = k
        min_capa = np.inf
        try:
            c = parent_list[v]
        except KeyError:
            return 0
        while v != s:
            parent = parent_list[v]
            edge = self.graph[parent][v]
            if edge.residual < min_capa:
                min_capa = edge.residual
            v = parent
        return min_capa

    def aug_path(self, s, k, parent_list, min_capa):
        v = k
        try:
            c = parent_list[v]
        except KeyError:
            return None
        while v != s:
            parent = parent_list[v]
            edge = self.graph[parent][v]
            virtual = self.graph[v][parent]
            edge.flow += min_capa
            edge.residual -= min_capa
            virtual.residual += min_capa
            v = parent

    def ford_fulkerson(self, start, end):
        max_flow = 0
        parent = self.bfs(start)
        min_capacity = self.analiz(start, end, parent)
        while min_capacity > 0:
            self.aug_path(start, end, parent, min_capacity)
            parent = self.bfs(start)
            min_capacity = self.analiz(start, end, parent)
        for v in self.graph[start]:
            max_flow += self.graph[start][v].flow
        return max_flow


def print_graph(g):
    n = g.order()
    print("------GRAPH------", n)
    for v1 in g.graph:
        print(v1.key, end=" -> ")
        for v2, edge in g.graph[v1].items():
                       print(v2.key, edge, end=";")
        print()
    print("-------------------")


graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20),
          ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
          ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
          ('d', 'c', 4)]
k = [2, 4, 6, 4]
g = [graf_0, graf_1, graf_2, graf_3]

for i in range(4):
    graf = g[i]
    test = GraphMatrix()
    for el in graf:
        v1 = Vertex(el[0])
        v2 = Vertex(el[1])
        edge = Edge(el[2])
        res_edge = Edge(0, True)
        test.insert_edge(v1, v2, edge)
        if v2 not in test.graph or v1 not in test.graph[v2]:
            test.insert_edge(v2, v1, res_edge)
    max_flow = test.ford_fulkerson(Vertex('s'), Vertex('t'))
    print(max_flow)
    print_graph(test)

