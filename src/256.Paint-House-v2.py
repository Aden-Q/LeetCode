class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        # paint all houses from index 0 to and include i
        # and paint house i with some color
        # returns the minimum cost
        @cache
        def dfs(i, color) -> int:
            if i == 0:
                return costs[0][color]

            min_cost = math.inf
            for prev_color in [0, 1, 2]:
                if prev_color == color:
                    continue
                min_cost = min(min_cost, dfs(i-1, prev_color))

            return min_cost + costs[i][color]

        return min(dfs(n-1, 0), dfs(n-1, 1), dfs(n-1, 2))