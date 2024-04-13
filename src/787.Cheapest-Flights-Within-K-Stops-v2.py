class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        prev = [float('inf')] * n
        curr = prev.copy()
        prev[src] = 0

        # at most k stops means at most k+1 edges
        for i in range(1, k+2):
            # iterate through all edges
            for start, end, cost in flights:
                curr[end] = min(prev[start] + cost, curr[end])
            
            prev = curr.copy()

        return curr[dst] if curr[dst] != float('inf') else -1
