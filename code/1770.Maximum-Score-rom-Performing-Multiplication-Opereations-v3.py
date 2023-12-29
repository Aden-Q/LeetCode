class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        # a 2d dp array
        dp = [[0] * (m+1) for _ in range(n+1)]
        for left in reversed(range(n)):
            for idx in reversed(range(left, m)):
                dp[left][idx] = max(nums[left] * multipliers[idx] + dp[left+1][idx+1], nums[n-1-(idx-left)] * multipliers[idx] + dp[left][idx+1])

        return dp[0][0]