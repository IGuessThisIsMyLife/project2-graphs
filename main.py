#Jonathan Nunes
#CS 435
#Project 2 Part 2

import random
from DirectedGraph import DirectedGraph
from TopSort import TopSort
from WeightedGraph import WeightedGraph
from GridGraph import GridGraph

def createRandomDAGIter(n):
    """Creates n random nodes with randomly assigned, unweighted, directed edges."""
    g = DirectedGraph()

    for i in range(n):

        g.addNode(i)

        if i < 2:
            continue

        edge = random.sample(g.getAllNodes(), 2)
        g.addDirectedEdge(min(edge), max(edge))

    return g

def createRandomCompleteWeightedGraph(n):
    """Makes a complete weighted graph where every node has an edge to every other node with randomly assigned weights."""
    g = WeightedGraph()

    for i in range(n):
        g.addNode(i)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            g.addWeightedEdge(i, j, random.choice(range(1, n)))

    return g

def createLinkedList(n):
    """Makes a weighted graph with n nodes, each having a single edge to the next node of uniform weight."""
    g = WeightedGraph()

    for i in range(n):

        g.addNode(i)

        if i == 0:
            continue
            
        g.addWeightedEdge(i-1, i, 1)

    return g

def dijkstras(start, graph):
    """Returns a dictionary mapping each node in the graph to the minimmum value from start to end node."""
    pass
##    distances = []
##
##    for node in graph.nodes:
##        
##        distances[node] = 100000
##        queue = []
##        
##        if node != start:
##            queue.append(node)
##            distances[start] = 0
##
##    while queue:
##        curr = queue.remove(min(queue))
##
##        for neighbor in graph.adjacency[curr]:

def createRandomGridGraph(n):
    """Creates n^2 random nodes with randomly assigned unweighted, bidirectional edges."""
    g = GridGraph()
    choices = [True, False]

    for y in range(n):
        for x in range(n):
            g.addGridNode(x, y, "(%i,%i)" % (x, y))

            if x != 0:
                if random.choice(choices):
                    g.addUndirectedEdge("(%i,%i)" % (x, y), "(%i,%i)" % (x - 1, y))

            if y != 0:
                if random.choice(choices):
                    g.addUndirectedEdge("(%i,%i)" % (x, y), "(%i,%i)" % (x, y - 1))

    return g

def astar(source, dest, graph):
    """Returns an ordered list from the source node to the destination node."""
    pass

def main():

    ###TESTING###
    d = createRandomDAGIter(10)
    w = createRandomCompleteWeightedGraph(10)
    l = createLinkedList(10)
    g = createRandomGridGraph(10)

    top = TopSort()
    tester = createRandomDAGIter(1000)
    grid = createRandomGridGraph(100)

    print("Random DAG and Edges:\n", d.adjacency)
    print("\nRandom Complete Weighted Graph and Edges:\n", w.adjacency)
    print("\nRandom Grid Graph and Edges:\n", g.adjacency)
    print("\nLinked List and Edges:\n", l.adjacency)
    print("\nKahn's Algorithm on DAG:\n", True if top.kahns(d) == sorted(top.kahns(d)) else False)
    print("\nmDFS Algorithm on DAG:\n", True if top.mDFS(tester) == sorted(top.mDFS(tester)) else False)
    #print("\nDijkstra's Algorithm on Complete Random Weighted Graph Starting From Node 3:\n", dijkstras(3, w))
    #print("\nA* Algorithm on Random Grid Graph:\n", astar("(0,0)", "(100,100)", grid))

if __name__ == "__main__":
    main()
