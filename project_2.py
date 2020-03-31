#Jonathan Nunes
#CS 435
#Project 2

import random

class Graph:

    def __init__(self):
        """Graph Constructor"""
        self.nodes = []
        self.adjacency = []

    def addNode(self, node):
        """Adds a new node to the graph"""
        self.nodes.append(node)
        self.adjacency.append([node])

    def addUndirectedEdge(self, first, second):
        """Adds an undirected edge between first and second nodes"""
        for node in self.adjacency:
            
            if node[0] == first:
                if second not in node:
                    node.append(second)
                    continue
                else:
                    return False
            
            if node[0] == second:
                if first not in node:
                    node.append(first)
                else:
                    return False

        return True

    def addDirectedEdge(self, first, second):
        """Adds a directed edge from first node to second node"""
        for node in self.adjacency:
            
            if node[0] == first:
                node.append(second)
                return

    def removeUndirectedEdge(self, first, second):
        """Removes an undirected edge between first and second nodes"""
        for node in self.adjacency:
            
            if node[0] == first:
                node.remove(second)
                continue
            
            if node[0] == second:
                node.remove(first)

    def getAllNodes(self):
        """Returns set of all nodes in the graph"""
        return self.nodes

class GraphSearch:

    def DFSRec(self, start, end, graph):
        """Recursively returns an ArrayList of the nodes in the graph in a valid DFS order"""
        visited = [False] * len(graph.nodes)

        DFSRecHelper(start, graph, visited)

    def DFSRecHelper(start, graph, visited):
        """"""
        pass
##        visited[start] = True
##
##
##        for node in graph.adjacency[start]:
##            if not visited

    def DFSIter(self, start, end, graph):
        """Iteratively returns an ArrayList of the nodes in the graph in a valid DFS order"""
        ret = [start]

        visited = [False] * len(graph.nodes)
        visited[start] = True

        stack = [start]

        while len(stack):
            start = stack[-1]
            stack.pop()

            if not visited[start]:
                ret.append(start)
                if start == end:
                    return ret
                visited[start] = True

            for node in graph.adjacency[start]:
                if not visited[node]:
                    stack.append(node)

        return None
                    
    def BFTRec(self, graph):
        """Recursively returns an ArrayList of the nodes in the graph in a valid BFT order"""
        pass

    def BFTIter(self, graph):
        """Iteratively returns an ArrayList of all of the nodes in the graph in a valid BFT order"""
        ret = []

        visited = [False] * len(graph.nodes)
        visited[graph.nodes[0]] = True

        queue = [graph.nodes[0]]

        while queue:

            start = queue.pop(0)
            ret.append(start)

            for node in graph.adjacency:
                for edge in node:
                    
                    if visited[edge] == False:
                        queue.append(edge)
                        visited[edge] = True

        return ret

class Main:

    def createRandomUnweightedGraphIter(self, n):
        """Creates 'n' random nodes with randomly assigned unweighted, bidirectional edges"""
        graph = Graph()
        
        for i in range(n):

            temp = random.choice(range(n))
            
            while temp in graph.nodes:
                temp = random.choice(range(n))
                
            graph.addNode(temp)

            if i < 2:
                continue

            edge = random.sample(graph.getAllNodes(), 2)

            while True:
                if graph.addUndirectedEdge(edge[0], edge[1]):
                    break
                else:
                    edge = random.sample(graph.getAllNodes(), 2)
                
        return graph            

    def createLinkedList(self, n):
        """Creates a directed graph with 'n' nodes where each node only has an edge to the next node created"""
        graph = Graph()
        
        for i in range(n):
            
            graph.addNode(i)
            
            if len(graph.nodes) == 1:
                continue
            
            graph.addDirectedEdge(i-1, i)
            
        return graph

    def BFTRecLinkedList(self, graph):
        """Runs a BFT recursively on a LinkedList"""
        l = createLinkedList(10000)

        s = GraphSearch()
        return s.BFTRec(l)

    def BFTIterLinkedList(self, graph):
        """Runs a BFT iteratively on a LinkedList"""
        l = createLinkedList(10000)

        s = GraphSearch()
        return s.BFTIter(l)

m = Main()
l = m.createLinkedList(10)
r = m.createRandomUnweightedGraphIter(10)
g = Graph()
s = GraphSearch()

for i in range(10):
    g.addNode(i)

for i in range(7):
    g.addUndirectedEdge(i, i + 3)

print("The adjancency array is formatted that index 0 in each array is the node and every number after is a node it has an edge to.\n")
print("LinkedList\n",l.adjacency)
print("\nRandom Unweighted Graph\n", r.adjacency)
print("\nGraph I Used For Testing\n", g.adjacency)
print("\nBFTIter on Random Unweighted Graph\n", s.BFTIter(r))
#print(s.BFTRec(r))
print("\nDFSIter on LinkedList (Works on any graph though)\n", s.DFSIter(1, 6, l))
#print(s.DFSRec(1, 6, r))
