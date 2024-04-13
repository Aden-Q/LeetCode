class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(n+1)]

        for j in range(1, k+1):
            dp[n][j][0] = -inf
            dp[n][j][1] = -inf
        
        for i in range(n-1, -1, -1):
            for j in range(k, 0, -1):
                flag = 1 if j % 2 == 1 else -1
                dp[i][j][1] = nums[i] * (j * flag) + max(dp[i+1][j-1][0], dp[i+1][j][1])
                dp[i][j][0] = max(dp[i+1][j][0], dp[i][j][1])

        return dp[0][k][0]
