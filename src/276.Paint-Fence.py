class Solution:
    def numWays(self, n: int, k: int) -> int:
        # colors are identified by 0 ~ k-1. There are k colors in total
        # i: the post we are currently at
        # returns the number of ways to paint i posts
        @lru_cache(None)
        def dp(i: int):
            if i == 0:
                return k
            if i == 1:
                return k ** 2

            # if we use a different color than the previous color
            # the number of ways to paint it is dp(i-1)
            # we have (k-1) * dp(i-1)
            # if we use the same color as the previous color
            # then i-2 must not use this color
            # given the symmetry, we can find the number of ways to paint it is dp(i-2) * (k-1) / k

            return (k-1) * (dp(i-1) + dp(i-2))

        return dp(n-1)
