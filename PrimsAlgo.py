
#This file contains all the fucntions to implement Prims Algo
#Created By Rohan Chopra

import time
import math

class prims(object):

    def __init__(self,v):
        self.minSpanningTree = []
        self.vistiedNodes = []
        self.v = v
        self.time = ""

    def runPrimsAlgoFor(self,adjMatrix):
        tic = time.time()  #Setting tic as current time
        currentVertex = 0  #Setting 0th node as the starting node
        EdgesFromCurrentVertex = []
        EdgeWithMinimuWeight = [None, None, math.inf] #Setting an edge with infinity weight

        while len(self.vistiedNodes) != self.v :
            self.vistiedNodes.append(currentVertex) #setting current as visited
            for i in range(0 , self.v): #To get all edges from current node
                if adjMatrix[currentVertex][i] != 0:
                    EdgesFromCurrentVertex.append([currentVertex,i,adjMatrix[currentVertex][i]])
            for i in range(0, len(EdgesFromCurrentVertex)):
                if EdgesFromCurrentVertex[i][2] < EdgeWithMinimuWeight[2] and EdgesFromCurrentVertex[i][1] not in self.vistiedNodes:
                    EdgeWithMinimuWeight = EdgesFromCurrentVertex[i]
            if EdgeWithMinimuWeight != [None, None, float('inf')]:
                self.minSpanningTree.append(EdgeWithMinimuWeight)
                EdgesFromCurrentVertex.remove(EdgeWithMinimuWeight)
                currentVertex = EdgeWithMinimuWeight[1]
                EdgeWithMinimuWeight = [None, None, float('inf')]
        tok = time.time()
        # To print on console
        t = "{0:.4f}".format(1000 * (tok - tic))
        print("Time :" + str(1000 * (tok - tic)) + "ms")
        self.time = "time :" + t + "ms"