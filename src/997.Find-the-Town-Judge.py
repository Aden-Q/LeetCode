class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdegrees = [0] * (n + 1)
        indegrees = [0] * (n + 1)
        for edge in trust:
            outdegrees[edge[0]] += 1
            indegrees[edge[1]] += 1
        for i in range(1, n+1):
            if outdegrees[i] == 0 and indegrees[i] == n-1:
                return i
        return -1