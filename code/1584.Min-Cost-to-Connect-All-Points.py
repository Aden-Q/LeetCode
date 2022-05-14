class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        self.parent[rootp] = rootq
        self.count -= 1
        return
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num = len(points)
        edge = []
        for i in range(num):
            for j in range(i + 1, num):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edge.append((i, j, dist))
        edge.sort(key = lambda x: x[2])
        
        uf = UF(num)
        total_cost = 0
        for e in edge:
            p, q, cost = e
            if uf.connected(p, q):
                continue
            uf.union(p, q)
            total_cost += cost
            # print(cost, ' ', uf.count)
            if uf.count == 1:
                break
        return total_cost