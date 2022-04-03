class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(3, n + 1):
            for j in range(1, i-1):
                dp[i] = max(dp[i], j * dp[i-j], (i-j) * j)
        return dp[n]