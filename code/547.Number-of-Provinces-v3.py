class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.num_groups = size

    # find the root of a node
    def find(self, x) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            # union two groups into one group
            self.num_groups -= 1
            self.parent[root_x] = self.parent[root_y]

    # test connectivity
    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def getNumGroups(self):
        return self.num_groups

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        # isConnected is an adjacency matrix, for an undirected graph, it must be symmetric
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        
        return uf.getNumGroups()
