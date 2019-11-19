
#This file contains all the fucntions to create a minimum Spanning Tree For Operations
#Created By Rohan Chopra

# THIS CLASS IS USED TO CREATE AN ADJACENCY MATRIX

class createGraphUsingAdjMatrix(object):

    def __init__(self, v):
        self.adjMatrix = []
        for i in range(0, v+1):
            self.adjMatrix.append([])
            for j in range(0, v+1):
                self.adjMatrix[i].append(0)


# TO ADD A SINGLE EDGE OF THE GRAPH TO ADJMATIX

    def addEdgesToGraph(self,v1 , v2 , w):

        if v1 != v2 :
            self.adjMatrix[v1][v2] = w
            self.adjMatrix[v2][v1] = w
        else:
            print("Error: self-loop cannot exist")

# TO RECURSIVELY ADD ALL INPUT EDGES TO ADJMATIX
    def addGraphToAdjMAtrix(self,G):
        for i in G:
            self.addEdgesToGraph(i[0],i[1],i[2])


# THIS CLASS IS USED TO CREATE A DISJOINT SET AND ITS ASSOCIATED FUNCTIONS

class CreateGraphUsingDisjointSets(object):

    def __init__(self,numberOfVertices):

        self.edgesOfGraph = []
        self.weightOfEdges = []
        self.vertexSet = []
        self.numberOfVertices = numberOfVertices

    # TO ADD A SINGLE EDGE OF THE GRAPH
    def addEdgesToGraph(self,StartVertex ,EndVertex ,weight):
        Edge = [StartVertex,EndVertex ,weight]

        if Edge not in self.edgesOfGraph:
            self.edgesOfGraph.append(Edge)
            self.weightOfEdges.append(weight)

    # MAKE SET FUNCTION
    def makeSet(self):
        for i in range(0,len(self.edgesOfGraph)):
            vertex = [self.edgesOfGraph[i][0]]
            vertex2 = [self.edgesOfGraph[i][1]]

            if vertex not in self.vertexSet:
                self.vertexSet.append(vertex)
            if vertex2 not in self.vertexSet:
                self.vertexSet.append(vertex2)

    # TO PERFORM SORTING
    def sortEdgesAndVertices(self):
        self.edgesOfGraph = sorted(self.edgesOfGraph,key=lambda x: x[2])
        self.weightOfEdges = sorted(self.weightOfEdges)

    # FIND SET FUNCTION
    def findSet(self,Vertex):
        for i in range(len(self.vertexSet)):
           for val in self.vertexSet[i]:
                if Vertex == val:
                    return i
        return None

    # UNION SET FUNCTION
    def unionSet(self,vertex1,vertex2):

        vertex1Index = self.findSet(vertex1)
        vertex2Index = self.findSet(vertex2)
        for vals in self.vertexSet[vertex2Index]:
            self.vertexSet[vertex1Index].append(vals)
        self.vertexSet.pop(vertex2Index)

    # TO RECURSIVELY ADD ALL INPUT EDGES TO ADJMATIX
    def addRecursively(self,g):
        for i in g:
            self.addEdgesToGraph(i[0],i[1],i[2])


# TO COUNT THE NUMBER OF VERTICES IN AN INPUT FILE GRAPH
def CountVertices(G):
    vertexSet=[]
    for i in range(0,len(G)):
        vertex = [G[i][0]]
        vertex2 = [G[i][1]]

        if vertex not in vertexSet:
            vertexSet.append(vertex)
        if vertex2 not in vertexSet:
            vertexSet.append(vertex2)
    return len(vertexSet)





