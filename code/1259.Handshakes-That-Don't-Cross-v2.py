class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (numPeople + 1)
        dp[0] = 1

        for i in range(1, numPeople + 1):
            for shake in range(1, i, 2):
                dp[i] += dp[shake-1] * dp[i - shake - 1]
                dp[i] = dp[i] % mod

        return dp[numPeople]
