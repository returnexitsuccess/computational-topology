#!/usr/bin/python3

# Testing for connectedness of a graph

import random


class Graph():
    def __init__(self, vertexList, edgeList):
        self.vertexList = vertexList
        self.edgeList = edgeList

        self._checkValid()

    def _checkValid(self):
        for edge in self.edgeList:
            if edge[0] not in self.vertexList:
                raise Exception(f"{edge[0]} not in vertex list")
            if edge[1] not in self.vertexList:
                raise Exception(f"{edge[1]} not in vertex list")

    def getComponents(self):
        self.nodes = {vertex: {"parent": vertex, "size": 1} for vertex in self.vertexList}
        for edge in self.edgeList:
            self.union(edge[0], edge[1])
        return len([vertex for vertex in self.nodes if self.nodes[vertex]["parent"] == vertex])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x != y:
            if self.nodes[x]["size"] > self.nodes[y]["size"]:
                self.nodes[y]["parent"] = x
                self.nodes[x]["size"] += self.nodes[y]["size"]
            else:
                self.nodes[x]["parent"] = y
                self.nodes[y]["size"] += self.nodes[x]["size"]

    def find(self, i):
        if self.nodes[i]["parent"] != i:
            self.nodes[i]["parent"] = self.find(self.nodes[i]["parent"])
            return self.nodes[i]["parent"]
        return i


def generateRandomGraph(numVertices, numEdges):
    vertexList = list(range(1, numVertices+1))
    allEdges = [(i, j) for i in vertexList for j in vertexList[i:]]
    edgeList = random.sample(allEdges, numEdges)
    return (vertexList, edgeList)


# Test what percentage of graphs with certain number of vertices and edges are connected
ITERS = 100
VERTS = 10
for numEdges in range(VERTS - 1, 1 + (VERTS - 1) * (VERTS - 2) // 2):
    numConnected = 0
    for j in range(ITERS):
        g = Graph(*generateRandomGraph(VERTS, numEdges))
        if g.getComponents() == 1:
            numConnected += 1
    print(f"{numEdges} Edges: {100 * numConnected / ITERS:.2f}%")
