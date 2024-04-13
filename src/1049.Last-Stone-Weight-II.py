class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumWeight = sum(stones)
        bagWeight = sumWeight // 2
        dp = [0] * (bagWeight + 1)
        for i in range(len(stones)):
            for j in range(bagWeight, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sumWeight - 2 * dp[-1]