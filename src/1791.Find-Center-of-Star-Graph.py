class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        in_degrees = [0] * (n + 1)
        for first, second in edges:
            in_degrees[first] += 1
            if in_degrees[first] == n - 1:
                return first
            in_degrees[second] += 1
            if in_degrees[second] == n - 1:
                return second
