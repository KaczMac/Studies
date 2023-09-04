import polska
class Vertex:
    def __init__(self,key) -> None:
        self.x = key[0]
        self.y = key[1]
        self.key = key[2]
    def __eq__(self,other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)

class AdjacencyMatrix:
    def __init__(self) -> None:
        self.sizee = 0
        self.neighbour_mat = [[]]
        self.vertices = []


    def isEmpty(self):
        return self.sizee == 0
    
    def insertVertex(self, vertex: Vertex):
        for row in self.neighbour_mat:
            row.append(0)
        if self.order() != 0:
            self.neighbour_mat.append([0] * (self.order() + 1))
        self.vertices.append(vertex)
        self.sizee += 1

    
    def insertEdge(self,vertex1,vertex2,edge=1):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.neighbour_mat[idx1][idx2] = edge
        self.neighbour_mat[idx2][idx1] = edge
        
    
    def deleteVertex(self,vertex):
        idx = self.getVertexIdx(vertex)
        self.vertices.pop(idx)
        for row in self.neighbour_mat:
            row.pop(idx)
        self.neighbour_mat.pop(idx)
        self.sizee -= 1
    
    def deleteEdge(self,vertex1,vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.neighbour_mat[idx1][idx2] = 0
        self.neighbour_mat[idx2][idx1] = 0

    
    def getVertexIdx(self,vertex):
        return self.vertices.index(vertex)

    def getVertex(self,vertex_idx):
        return self.vertices[vertex_idx]
    
    def neighbours(self,vertex_idx):
        neighbours = []
        for i,v in enumerate(self.neighbour_mat[vertex_idx]):
            if v != 0:
                neighbours.append(i)
        return neighbours

    def order(self):
        return len(self.vertices)
    
    def size(self):
        sizes = 0
        for row in self.neighbour_mat:
            sizes += sum(row)
        return int(sizes/2)
    
    def edges(self):
        edges = []
        for i in range(self.order()):
            for j in range(i,self.order()):
                if self.neighbour_mat[i][j] != 0:
                    edges.append((self.getVertex(i).key, self.getVertex(j).key))
        return edges


class AdjacencyList:
    def __init__(self) -> None:
        self.sizee = 0
        self.neighbour_lst = []
        self.vertices = []

    def isEmpty(self):
        return self.sizee == 0
    
    def insertVertex(self, vertex: Vertex):
        self.vertices.append(vertex)
        self.neighbour_lst.append([])
        

    
    def insertEdge(self,vertex1,vertex2,edge=1):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.neighbour_lst[idx1].append(idx2)
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
        self.neighbour_lst[idx1].remove(idx2)
        self.neighbour_lst[idx2].remove(idx1)
        self.sizee -= 1

    
    def getVertexIdx(self,vertex):
        return self.vertices.index(vertex)

    def getVertex(self,vertex_idx):
        return self.vertices[vertex_idx]
    
    def neighbours(self,vertex_idx):
        idx = self.getVertexIdx(vertex_idx)
        return self.neighbour_lst[idx]

    def order(self):
        return len(self.vertices)
    
    def size(self):
        sizes = 0
        for row in self.neighbour_mat:
            sizes += sum(row)
        return sizes//2
    
    def edges(self):
        edges = []
        for i in range(len(self.neighbour_lst)):
            for j in self.neighbour_lst[i]:
                edges.append((self.getVertex(i).key, self.getVertex(j).key))
        return edges


graphl = AdjacencyList()
graphm = AdjacencyMatrix()

for v1,v2 in polska.graf:
    v1 = Vertex(polska.slownik[v1])
    v2 = Vertex(polska.slownik[v2])
    graphm.insertVertex(v1)
    graphm.insertVertex(v2)
    graphm.insertEdge(v1,v2)
    graphl.insertVertex(v1)
    graphl.insertVertex(v2)
    graphl.insertEdge(v1,v2)

graphm.deleteEdge(Vertex(polska.slownik['W']), Vertex(polska.slownik['E']))
graphm.deleteVertex(Vertex(polska.slownik['K']))
polska.draw_map(graphm.edges())

graphl.deleteVertex(Vertex(polska.slownik['K']))
graphl.deleteEdge(Vertex(polska.slownik['W']), Vertex(polska.slownik['E']))
polska.draw_map(graphl.edges())
