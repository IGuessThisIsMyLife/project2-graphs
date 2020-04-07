# Project 2 - Graphs
<pre>
Questions 1 - 2

1.a.)
S -> A -> C, B, E -> F -> G -> K -> L -> D

b.)
S: A
A: B, C, E, S 
C: A
B: A, E
E: A, B, F
F: E, G
G: F, K
K: G, L
L: K, D
D: L

c.)
    A
  /   \
S - B - D
  \   /
    C


2.a.)
Number of Nodes: 25

b.)
Edges would be the adjacent tiles to the current tile being visited.

c.)
Graph Properties: Undirected, Connected

d.)
                        8       
                      /       
                    7       10 - 11 - 12
                  /   \   /
                6       9
              /           \
            5               13 - 14 - 15
          /                   
        4                       
      /                           
    3                       21
  /                       /
S - 16 - 17 - 18 - 19 - 20
  \                       \
    1                       22
      \                       \
        2                       23
                                  \
                                    D


3.h.i.)
The issue that would be ran into would be the implicit space growing too large for a computer to handle since it's O(n) implicit space.

i.)
This won't have the same issue of implicit space since it's not recursive.

4.a.) Properties of a Directed Acyclic Graph:
i.) Contains no cycles
ii.) Nodes have edges towards a node greater than itself

5.a.) Because the edges have weights, Dijkstra’s algorithm can be used to derive a shortest path. Also, because it’s complete, there are no disconnected nodes so every node can be reached.

6.c.) The best path will either consist of moving to the right or up because the end point is in the opposite corner, thus those are the only directions I need to examine when pathfinding.
</pre>



