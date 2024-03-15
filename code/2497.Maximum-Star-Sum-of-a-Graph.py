class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        # build the graph
        graph = [[] for _ in range(n)]
        for first, second in edges:
            # greedy, if the node's value is <= 0 then we don't care about it, it's better to discard the edge
            if vals[second] > 0:
                heapq.heappush(graph[first], vals[second])
                if len(graph[first]) > k:
                    heapq.heappop(graph[first])

            if vals[first] > 0:
                heapq.heappush(graph[second], vals[first])
                if len(graph[second]) > k:
                    heapq.heappop(graph[second])
            
        max_star_sum = -float('inf')
        for i in range(n):
            max_star_sum = max(max_star_sum, vals[i] + sum(graph[i]))

        return max_star_sum
