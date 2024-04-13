class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for road in roads:
            degrees[road[0]] += 1
            degrees[road[1]] += 1
        degrees.sort()
        cul_sum = 0
        for i in range(n, 0, -1):
            cul_sum += degrees[i-1] * i
        return cul_sum