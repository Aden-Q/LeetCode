class Solution:
    def maxA(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        # dp[i] represents the maximum number of A we can get when we press i times
        for i in range(n):
            for j in range(i+3, min(n, i+6) + 1):
                dp[j] = max(dp[j], (j-i-1) * dp[i])
        
        return dp[n]
