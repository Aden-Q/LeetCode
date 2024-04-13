class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0] * len(values)
        dp[0] = 0
        dp[1] = values[1] + values[0] - 1
        
        # dp[j] represents the maximal score using values[j] and another stop with index 0 <= i < j
        for j in range(2, len(values)):
            dp[j] = max(dp[j-1] - values[j-1] + values[j] + (j-1) - (j), values[j-1] + values[j] - 1)
            
        return max(dp)