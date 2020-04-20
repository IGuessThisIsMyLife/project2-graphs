#Jonathan Nunes
#CS 435
#Project 2 Part 2
#Weighted Graph Class

class WeightedGraph:

    def __init__(self):
        """Weighted Graph Constructor"""
        self.nodes = set()
        self.adjacency = {}
        self.weights = {}

    def addNode(self, node):
        """Adds a new node to the graph."""
        self.nodes.add(node)
        self.adjacency[node] = [] 

    def addWeightedEdge(self, first, second, weight):
        """Adds a directed, weighted edge between first and second."""
        if first in self.adjacency:
            if second not in self.adjacency[first]:
                self.adjacency[first].append(second)
                self.weights[str(first) + " --> " + str(second)] = weight 
            
    def removeDirectedEdge(self, first, second):
        """Removes a directed, weighted edge between first and second."""
        if first in self.adjacency:
            if second in self.adjacency[first]:
                self.adjacency[first].remove(second)
                self.weights.pop(str(first) + " --> " + str(second)) 

    def getAllNodes(self):
        """Returns set of all nodes."""
        return self.nodes
