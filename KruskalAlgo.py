

#This file contains all the fucntions to implement Kruskal's Algo
#Created By Rohan Chopra

import DataStructures as DS
import time

class kruskalAlgo(object):

    def __init__(self, numberOfVertices):
        self.MST = []
        self.DS = DS.CreateGraphUsingDisjointSets(numberOfVertices)
        self.time = ""

    def FindMST(self):
        self.DS.makeSet() #Make a disjoint Set
        tic = time.time()
        self.DS.sortEdgesAndVertices()
        for i in self.DS.edgesOfGraph:
            if self.DS.findSet(i[0]) != self.DS.findSet(i[1]):
                self.MST.append(i)
                self.DS.unionSet(i[0],i[1])
        tok = time.time()
        # To print on console
        t ="{0:.4f}".format(1000 * (tok - tic))
        print("Time :" + str(1000 * (tok - tic)) + "ms")
        self.time = "time :" + t + "ms"
