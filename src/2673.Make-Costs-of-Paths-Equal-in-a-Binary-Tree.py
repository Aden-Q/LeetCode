class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        total_cost = 0

        for idx in range(n, 1, -2):
            # each time we combine 2 nodes and add their new cost to its parent
            total_cost += abs(cost[idx-1] - cost[idx-2])
            cost[idx // 2 - 1] += max(cost[idx-1], cost[idx-2])

        return total_cost
