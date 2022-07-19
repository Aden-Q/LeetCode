class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [0, 0, 0]
        # dp[i] represents the minimum cost of painting all the houses
        # up to the current house, with the current house paint by:
        # index 0: red
        # index 1: blue
        # index 2: green
        # Initialize dp by:
        dp[0] = costs[0][0]
        dp[1] = costs[0][1]
        dp[2] = costs[0][2]
        next_dp = [0, 0, 0]
        for i in range(1, n):
            next_dp[0] = min(dp[1], dp[2]) + costs[i][0]
            next_dp[1] = min(dp[2], dp[0]) + costs[i][1]
            next_dp[2] = min(dp[0], dp[1]) + costs[i][2]
            # copy back
            dp = next_dp.copy()
        return min(dp)