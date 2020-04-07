#Jonathan Nunes
#CS 435
#Project 2 Part 2
#Top Sort Class

class TopSort:

    def kahns(self, graph):
        """Does a valid topological sort of the graph using Kahn's algorithm."""
        dependencies = {}
        for node in graph.nodes:
            dependencies[node] = len(graph.adjacency[node])

        ret = []

        queue = []
        for node in graph.nodes:
            if dependencies[node] == 0:
                queue.append(node)

        while queue:

            temp = queue.pop(0)
            ret.append(temp)

            dependencies[temp] = -1
            for node in graph.adjacency[temp]:
                dependencies[node] -= 1

                if dependencies[node] == 0:
                    queue.append(node)

        return ret

    def mDFS(self, graph):
        """Does a valid topological sort of the graph using mDFS algorithm."""
        stack = []
        visited = [False] * len(graph.nodes)

        for node in graph.nodes:
            if visited[node] == False:
                self.mDFSHelper(graph, node, visited, stack)
                
        return stack

    def mDFSHelper(self, graph, node, visited, stack):
        """Helper function for the mDFS function."""
        visited[node] = True

        for neighbor in graph.adjacency[node]:
            if visited[neighbor] == False:
                self.mDFSHelper(graph, neighbor, visited, stack)
                
        stack.append(node)