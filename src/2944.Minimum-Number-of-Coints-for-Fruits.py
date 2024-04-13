class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)

        # state: current index and number of free fruits we can take from here
        # returns the minimum cost to acquire all fruits start from the given index
        @cache
        def dp(start, num_free) -> int:
            if start == n:
                return 0

            if num_free == 0:
                # we have to purchase the current fruit
                return prices[start] + dp(start+1, start+1)
            
            # otherwise we have 2 choices, purchase the current fruit or take it free
            return min(prices[start] + dp(start+1, start+1), dp(start+1, num_free-1))

        return dp(0, 0)
