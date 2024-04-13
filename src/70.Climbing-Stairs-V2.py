class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        weights = [1, 2]
        for i in range(n + 1):
            for j in weights:
                if i >= j:
                    dp[i] += dp[i-j] 
        return dp[n]