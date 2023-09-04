import numpy as np
from copy import deepcopy
class Vertex:
    def __init__(self,key) -> None:
        self.key = key
    def __eq__(self,other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)
    def __repr__(self) -> str:
        return str(self.key)

class AdjacencyMatrix:
    def __init__(self) -> None:
        self.sizee = 0
        self.neighbour_mat = [[]]
        self.vertices = []

    def isEmpty(self):
        return self.sizee == 0
    
    def insertVertex(self, vertex: Vertex):
        if vertex not in self.vertices:
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
    
    def getNeighbourMat(self):
        return self.neighbour_mat
    
    def edges(self):
        edges = []
        for i in range(self.order()):
            for j in range(i,self.order()):
                if self.neighbour_mat[i][j] != 0:
                    edges.append((self.getVertex(i).key, self.getVertex(j).key))
        return edges
    
def is_iso(g,p,m):
        x = m @ np.transpose(m@g)
        if np.array_equal(x, p):
            return True
        else:
            return False

def ullmann1(g, p, M=None,crow =0,used_cloumns=[], no_recursion = 0, isomorphism =[]):
    no_recursion += 1
    if M is None:
        M = np.zeros((p.shape[0], g.shape[0]))
    if crow == np.shape(M)[0]:
        if is_iso(g,p,M):
            isomorphism.append(M)
        return isomorphism, no_recursion
    for c in range(np.shape(M)[1]):
        if c not in used_cloumns:
            used_cloumns.append(c)
            M[crow][:] = 0
            M[crow][c] = 1
            isomorphism, no_recursion = ullmann1(g, p, M, crow+1, used_cloumns, no_recursion, isomorphism)
            used_cloumns.remove(c)
    return isomorphism, no_recursion



def M0(g,p):
    m0 = np.zeros((p.shape[0], g.shape[0]))
    for i in range(p.shape[0]):
        for j in range(g.shape[0]):
            if deg(p,i) <= deg(g,j):
                m0[i][j] = 1
    return m0

def deg(matrix, row):
    edges = 0
    for i in range(matrix.shape[0]):
        if matrix[row][i] == 1:
            edges += 1
    return edges

def ullmann2(g, p, m0, M=None,crow =0,used_cloumns=[], no_recursion = 0, isomorphism =[]):
    no_recursion += 1
    if M is None:
        M = np.zeros((p.shape[0], g.shape[0]))
    if crow == np.shape(M)[0]:
        if is_iso(g,p,M):
            isomorphism.append(M)
        return isomorphism, no_recursion
    for c in range(np.shape(M)[1]):
        if c not in used_cloumns and m0[crow][c] == 1:
            used_cloumns.append(c)
            M[crow][:] = 0
            M[crow][c] = 1
            isomorphism, no_recursion = ullmann2(g, p, m0, M, crow+1, used_cloumns, no_recursion, isomorphism)
            used_cloumns.remove(c)
    return isomorphism, no_recursion

def prune(g, p, m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i][j] == 1:
                neighbors_P = []
                for k in range(p.shape[0]):
                    if p[i][k] == 1:
                        neighbors_P.append(k)
                neighbors_G = []
                for l in range(g.shape[0]):
                    if g[j][l] == 1:
                        neighbors_G.append(l)
                for x in neighbors_P:
                    temp = False
                    for y in neighbors_G:
                        if m[x][y] == 1:
                            temp = True
                            break
                    if temp:
                        break
                else:
                    m[i][j] = 0
                    return True
    return False


def ullmann3(g, p, m0, M=None,crow =0,used_cloumns=[], no_recursion = 0, isomorphism =[]):
    no_recursion += 1
    if M is None:
        M = np.zeros((p.shape[0], g.shape[0]))
    if crow == np.shape(M)[0]:
        if is_iso(g,p,M):
            isomorphism.append(M)
        return isomorphism, no_recursion
    Mc = M.copy()
    temp = False
    if crow == np.shape(M)[0] - 1:
        temp = prune(g,p,Mc)
    for c in range(np.shape(M)[1]):
        if temp == True:
            break
        if c not in used_cloumns and m0[crow][c] == 1:
            used_cloumns.append(c)
            Mc[crow][:] = 0
            Mc[crow][c] = 1
            isomorphism, no_recursion = ullmann3(g, p, m0, Mc, crow+1, used_cloumns, no_recursion, isomorphism)
            used_cloumns.remove(c)
    return isomorphism, no_recursion
def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    graph_g = AdjacencyMatrix()
    for el in graph_G:
        v1 = Vertex(el[0])
        v2 = Vertex(el[1])
        graph_g.insertVertex(v1)
        graph_g.insertVertex(v2)
        graph_g.insertEdge(v1,v2)
        graph_g.insertEdge(v2,v1)
    graph_p = AdjacencyMatrix()
    for el in graph_P:
        v1 = Vertex(el[0])
        v2 = Vertex(el[1])
        graph_p.insertVertex(v1)
        graph_p.insertVertex(v2)
        graph_p.insertEdge(v1,v2)
        graph_p.insertEdge(v2,v1)
    G = np.array(graph_g.neighbour_mat)
    P = np.array(graph_p.neighbour_mat)
    iso, recursion = ullmann1(G,P)
    print(iso, "\n", recursion)
    m0 = M0(G,P)
    
    iso2, recursion2 = ullmann2(G,P,m0)
    print(iso2, "\n", recursion2)
    iso3, recursion3 = ullmann3(G,P,m0)
    print(iso3, "\n", recursion3)
main()