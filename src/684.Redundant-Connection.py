class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def union(self, key1, key2):
        if not self.isConnected(key1, key2):
            root1 = self.find(key1)
            root2 = self.find(key2)
            self.parent[root1] = root2
    
    def find(self, key):
        while self.parent[key] != key:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key
        
    def isConnected(self, key1, key2):
        return self.find(key1) == self.find(key2)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n + 1)
        for edge in edges:
            p, q = edge
            if uf.isConnected(p, q):
                return edge
            uf.union(p, q)
        