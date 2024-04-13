import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pairs = []
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            pairs.append((sum(mat[i]), i))
        heapq.heapify(pairs)
        res = []
        res = heapq.nsmallest(k, pairs)
        return [a[1] for a in res]