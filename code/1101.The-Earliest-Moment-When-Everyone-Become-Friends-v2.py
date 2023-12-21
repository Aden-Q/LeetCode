class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.num_groups = size

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            # union
            self.parent[root_x] = root_y
            self.num_groups -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def getNumGroups(self):
        return self.num_groups

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # sort the logs by timestamp, in ascending order
        logs.sort(key = lambda x: x[0])
        uf = UnionFind(n)

        for log in logs:
            timestamp, first, second = log
            uf.union(first, second)
            if uf.getNumGroups() == 1:
                return timestamp

        return -1