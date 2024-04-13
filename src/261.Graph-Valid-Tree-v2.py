class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        self.parent[root_x] = self.parent[root_y]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # we can use DSU to solve the problem
        # the graph is not tree means that:
        # either the number of connected components is > 1
        # or there is at least cycle in a component
        # a cycle means we attempt to union two connected components
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for first, second in edges:
            if uf.connected(first, second):
                # found a cycle
                return False
            uf.union(first, second)

        return True
