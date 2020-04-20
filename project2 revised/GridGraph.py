#Jonathan Nunes
#CS 435
#Project 2 Part 2
#Grid Graph Class

class GridGraph:

    def __init__(self):
        """Grid Graph Constructor"""
        self.nodes = []
        self.adjacency = {}
        self.coordinates = {}

    def addGridNode(self, x, y, node):
        """Adds a new GridNode to the graph with coordinates x and y."""
        self.nodes.append(node)
        self.adjacency[node] = []
        self.coordinates[node] = [x, y]

    def addUndirectedEdge(self, first, second):
        """Adds an undirected, unweighted edge between first and second."""
        if self.isNeighbor(first, second):
            if (first in self.adjacency) and (second in self.adjacency):
                if first not in self.adjacency[second]:
                    self.adjacency[first].append(second)
                    self.adjacency[second].append(first)

    def removeUndirectedEdge(self, first, second):
        """Removes an undirected edge between first and second."""
        if (first in self.adjacency) and (second in self.adjacency):
            if first in self.adjacency[second]:
                self.adjacency[first].remove(second)
                self.adjacency[second].remove(first)

    def getAllNodes(self):
        """Returns a set of all GridNodes in the graph."""
        return self.nodes

    def isNeighbor(self, first, second):
        """Helps determine if two nodes are neighbors."""
        if abs(self.coordinates[first][0] - self.coordinates[second][0]) == 0 and \
           abs(self.coordinates[first][1] - self.coordinates[second][1]) == 1 or \
           abs(self.coordinates[first][0] - self.coordinates[second][0]) == 1 and \
           abs(self.coordinates[first][1] - self.coordinates[second][1]) == 0:
            return True
        else:
            return False
