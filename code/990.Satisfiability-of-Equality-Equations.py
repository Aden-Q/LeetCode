class UF:
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
        
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        self.parent[root_p] = root_q
        self.count -= 1
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        candidates = []
        for eq in equations:
            op1 = ord(eq[0]) - ord('a')
            op2 = ord(eq[3]) - ord('a')
            if eq[1] == '=':
                uf.union(op1, op2)
            elif eq[1] == '!':
                candidates.append((op1, op2))
        # conflict candidates
        for p in candidates:
            op1, op2 = p[0], p[1]
            if uf.find(op1) == uf.find(op2):
                return False
        return True