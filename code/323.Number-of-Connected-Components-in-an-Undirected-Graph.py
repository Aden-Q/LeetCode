class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.num_groups = size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = self.parent[root_y]
            self.num_groups -= 1
        
        return

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def getNumGroups(self):
        return self.num_groups

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for first, second in edges:
            uf.union(first, second)
        
        return uf.getNumGroups()
        