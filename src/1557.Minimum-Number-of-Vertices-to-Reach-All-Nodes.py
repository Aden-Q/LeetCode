class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        for edge in edges:
            indegrees[edge[1]] += 1
        res = []
        for i in range(n):
            if indegrees[i] == 0:
                res.append(i)
        return res