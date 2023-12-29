class Solution:
    def numWays(self, n: int, k: int) -> int:
        # colors are identified by 0 ~ k-1. There are k colors in total
        # i: the post we are currently at
        # returns the number of ways to paint i posts
        if n == 1:
            return k

        dp_prev, dp_prev_prev = k * k,  k
        for i in range(2, n):
            dp_prev_prev, dp_prev = dp_prev, (k-1) * (dp_prev+ dp_prev_prev)

        return dp_prev
