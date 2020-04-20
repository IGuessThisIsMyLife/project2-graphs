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
    graph = DirectedGraph()

    for i in range(n):
        graph.addNode(i)
        if i < 2:
            continue
        edge = random.sample(graph.getAllNodes(), 2)
        while not graph.addDirectedEdge(min(edge), max(edge)):
            edge = random.sample(graph.getAllNodes(), 2)

    return graph

def createRandomCompleteWeightedGraph(n):
    """Makes a complete weighted graph where every node has an edge to every other node with randomly assigned weights."""
    graph = WeightedGraph()

    for i in range(n):
        graph.addNode(i)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            graph.addWeightedEdge(i, j, random.choice(range(1, n)))

    return graph

def createLinkedList(n):
    """Makes a weighted graph with n nodes, each having a single edge to the next node of uniform weight."""
    graph = WeightedGraph() 

    for i in range(n):
        graph.addNode(i)
        if i == 0:
            continue
        graph.addWeightedEdge(i-1, i, 1)

    return graph

def dijkstras(start, graph):
    """Returns a dictionary mapping each node in the graph to the minimmum value from start to end node."""
    pass
## TODO:
    distances = []

    for node in graph.nodes:
        
        distances[node] = 100000
        queue = []
        
        if node != start:
            queue.append(node)
            distances[start] = 0

    while queue:
        curr = queue.remove(min(queue))

def createRandomGridGraph(n):
    """Creates n^2 random nodes with randomly assigned unweighted, bidirectional edges."""
    graph = GridGraph()
    choices = [True, False]

    for y in range(n):
        for x in range(n):
            graph.addGridNode(x, y, "(%i,%i)" % (x, y))

            if x != 0:
                if random.choice(choices):
                    graph.addUndirectedEdge("(%i,%i)" % (x, y), "(%i,%i)" % (x - 1, y))

            if y != 0:
                if random.choice(choices):
                    graph.addUndirectedEdge("(%i,%i)" % (x, y), "(%i,%i)" % (x, y - 1))

    return graph

def astar(source, dest, graph):
    """Returns an ordered list from the source node to the destination node."""
    pass
## TODO:

def main():

    ###TESTING###
    directed = createRandomDAGIter(25)
    weighted = createRandomCompleteWeightedGraph(10)
    linked = createLinkedList(10)
    grid = createRandomGridGraph(10)

    top = TopSort()
    tester = createRandomDAGIter(1000)
    gridgraph = createRandomGridGraph(100)

    print("Random DAG and Edges:\n", directed.adjacency)
    print("\nRandom Complete Weighted Graph and Edges:\n", weighted.adjacency)
    print("\nRandom Grid Graph and Edges:\n", grid.adjacency)
    print("\nLinked List and Edges:\n", linked.adjacency)
    print("\nKahn's Algorithm on DAG:\n", top.kahns(directed))
    print("\nmDFS Algorithm on DAG:\n", True if top.mDFS(tester) == sorted(top.mDFS(tester)) else False)
    #print("\nDijkstra's Algorithm on Complete Random Weighted Graph Starting From Node 3:\n", dijkstras(3, w))
    #print("\nA* Algorithm on Random Grid Graph:\n", astar("(0,0)", "(99,99)", gridgraph))

if __name__ == "__main__":
    main()
