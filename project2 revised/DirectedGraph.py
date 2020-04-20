#Jonathan Nunes
#CS 435
#Project 2 Part 2
#Directed Graph Class

class DirectedGraph:

    def __init__(self):
        """Directed Graph Constructor"""
        self.nodes = []
        self.adjacency = {}

    def addNode(self, node):
        """Adds a new node to the graph"""
        self.nodes.append(node)
        self.adjacency[node] = []

    def addDirectedEdge(self, first, second):
        """Adds a directed edge between first and second."""
        if first in self.adjacency:
            if second not in self.adjacency[first]:
                self.adjacency[first].append(second)
                return True
        return False

    def removeDirectedEdge(self, first, second):
        """Removes a directed edge between first and second."""
        if first in self.adjacency:
            if second in self.adjacency[first]:
                self.adjacency[first].remove(second)

    def getAllNodes(self):
        """Returns set of all nodes."""
        return self.nodes
