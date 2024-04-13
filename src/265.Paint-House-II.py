class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])

        # i: the current house we are paining
        # color: color of the current house
        # returns the minimum cost to pain house from index 0 up to and include index i
        # and using color to paint the house i
        @cache
        def dp(i, color) -> int:
            if i == 0:
                # no way to paint house, beyond the boundary
                return costs[0][color]

            min_cost = math.inf
            for prev_color in range(k):
                if prev_color == color:
                    continue
                min_cost = min(min_cost, dp(i-1, prev_color))

            return min_cost + costs[i][color]

        min_cost = math.inf
        for color in range(k):
            min_cost = min(min_cost, dp(n-1, color))

        return min_cost