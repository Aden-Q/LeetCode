class UF:
    def __init__(self, size):
        # to start, each node is its own parent
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        self.parent[root_x] = root_y

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # We'll be using the Union and Find algorithm to test bipartite graph.
        # The idea's following:
        # enumerate each edge in the graph, those 2 endpoints must belong to two separate connected components
        # If we ever encounter an edge such that contracts with the above property ^, this graph is not bipartite
        # More over, if the graph itself is not a connected, the graph is not bipartite.
        # With what's said above, attempt to make the graph into 2 separate connected components. If we cannot,
        # the graph is not bipartite
        n = len(graph)
        uf = UF(n)

        for row in graph:
            length = len(row)
            for i in range(1, length):
                uf.union(row[0], row[i])

        for first in range(n):
            for second in graph[first]:
                if uf.connected(first, second):
                    return False

        return True
