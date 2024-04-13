class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we only need to maintain a 1-D array and go down by 1 level at each iteration
        dp = [1] * n
        # we need to go down m - 1 times until we reach the last row
        for _ in range(m-1):
            # from left to right
            for col in range(1, n):
                dp[col] = dp[col] + dp[col-1]

        return dp[-1]
         