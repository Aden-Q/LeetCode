class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # we should re-paint a painted house
        m, n = len(cost), len(cost[0])

        # idx: idx of the current house we're painting
        # next_color: the color of the next house
        # num_groups: the current number of neighborhoods for houses[idx+1:]
        # returns the minimum cost of painting all houses up to and include houses[idx] to form exactly target groups
        @cache
        def dp(idx, next_color, num_groups) -> int:
            if num_groups > target:
                # the current number of groups is too big, trim the search space
                return math.inf

            if idx == -1:
                if num_groups == target:
                    return 0
                else:
                    return math.inf

            # otherwise we invoke recursive calls
            # we need to choose a color to paint the current house, then use idx - 1 to optimally paint the previous house
            # first check if the current house can be painted
            if houses[idx] != 0:
                if houses[idx] == next_color:
                    # no new groups added
                    return dp(idx-1, houses[idx], num_groups)
                else:
                    # one more new group
                    return dp(idx-1, houses[idx], num_groups+1)
            
            min_cost = math.inf
            for color in range(1, n+1):
                if color == next_color:
                    # no new group added
                    min_cost = min(min_cost, cost[idx][color-1] + dp(idx-1, color, num_groups))
                else:
                    # one more new group
                    min_cost = min(min_cost, cost[idx][color-1] + dp(idx-1, color, num_groups+1))

            return min_cost

        # we want to pain all houses up to index m -1 which is the last house
        # initially the number of groups to the right of house m-1 is 0 (no house)
        # next color is set to some random non-existing color
        min_cost = dp(m-1, 0, 0)
        return min_cost if min_cost != math.inf else -1
