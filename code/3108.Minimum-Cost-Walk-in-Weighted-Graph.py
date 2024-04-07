class UnionFind():
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.bits = [int('11111111111111111', 2) for _ in range(size)]
        self.msb = [0 for _ in range(size)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        
        # new root is root_x
        self.parent[root_y] = root_x
        self.msb[root_x] = max(self.msb[root_x], self.msb[root_y])
        self.bits[root_x] &= self.bits[root_y]

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def insert(self, x, weight):
        root_x = self.find(x)
        self.msb[root_x] = max(self.msb[root_x], weight.bit_length())
        self.bits[root_x] &= weight
        
    def getDist(self, x):
        root_x = self.find(x)
        return self.bits[root_x] if self.msb[root_x] else 0
    

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        uf = UnionFind(n)
        for start, end, weight in edges:
            uf.union(start, end)
            uf.insert(start, weight)
        
        res = []
        for start, end in query:
            if not uf.connected(start, end):
                res.append(-1)
            elif start == end:
                res.append(0)
            else:
                res.append(uf.getDist(start))
            
        return res
