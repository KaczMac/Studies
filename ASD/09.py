import graf_mst
class Vertex:
    def __init__(self,key, color=0) -> None:
        self.key = key
        self.color = color
    def __eq__(self,other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)
    def __repr__(self):
        return str(self.key)


class AdjacencyList:
    def __init__(self) -> None:
        self.sizee = 0
        self.neighbour_lst = []
        self.vertices = []

    def isEmpty(self):
        return self.sizee == 0
    
    def insertVertex(self, vertex: Vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.neighbour_lst.append([])
    
    def insertEdge(self, vertex1, vertex2, edge):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            idx1 = self.getVertexIdx(vertex1)
            idx2 = self.getVertexIdx(vertex2)
            self.neighbour_lst[idx1].append((idx2, edge))
            self.neighbour_lst[idx2].append((idx1, edge))
            self.sizee += 1


    def deleteVertex(self,vertex):
        idx = self.getVertexIdx(vertex)
        self.vertices.remove(vertex)
        del self.neighbour_lst[idx]
        for i in self.neighbour_lst:
            if idx in i:
                i.remove(idx)
    
    def deleteEdge(self,vertex1,vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        edge = self.getEdge(vertex1,vertex2)
        self.neighbour_lst[idx1].remove((idx2,edge))
        self.neighbour_lst[idx2].remove((idx1,edge))
        self.sizee -= 1

    def getVertexColor(self,vertex):
        return vertex.color

    def setVertexColor(self,vertex,color):
        vertex.color = color

    def getEdge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.vertices:
            idx1 = self.getVertexIdx(vertex1)
            idx2 = self.getVertexIdx(vertex2)
            for edge in self.neighbour_lst[idx1]:
                if edge[0] == idx2:
                    return edge[1]
            return None

    def getVertexIdx(self,vertex):
        return self.vertices.index(vertex)

    def getVertex(self,vertex_idx):
        return self.vertices[vertex_idx]
    
    def neighbours(self,vertex_idx):
        return self.neighbour_lst[vertex_idx]

    def order(self):
        return len(self.vertices)
    
    def size(self):
        return len(self.vertices)

    def prim_mst(self,v):
        MST = AdjacencyList()
        for i in self.vertices:
            MST.insertVertex(i)
        size = len(self.vertices)
        intree = [0] * size
        distance = [float('inf')] * size
        parent = [-1] * size
        v = self.getVertexIdx(v)
        while intree[v] == 0:
            intree[v] = 1
            neighborhood = self.neighbours(v)
            for i in neighborhood:
                if intree[i[0]] == 0 and i[1] < distance[i[0]]:
                    distance[i[0]] = i[1]
                    parent[i[0]] = v
            
            minimal = float('inf')
            for vertex in range(size):
                if intree[vertex] == 0 and distance[vertex] < minimal:
                    minimal = distance[vertex]
                    next_vertex = vertex
            if minimal != float('inf'):
                MST.insertEdge(self.vertices[parent[next_vertex]],self.vertices[next_vertex],minimal)
            v = next_vertex
        total_weight = 0
        for i in distance:
            if i != float('inf'):
                total_weight += i
        return MST, total_weight

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")

def main():
    graph = AdjacencyList()
    graph_c = graf_mst.graf

    for el in graph_c:
        graph.insertVertex(Vertex(el[0]))
        graph.insertVertex(Vertex(el[1]))
        graph.insertEdge(Vertex(el[0]),Vertex(el[1]),el[2])

    mst, total_weight = graph.prim_mst(Vertex('G'))
    printGraph(mst)
main()