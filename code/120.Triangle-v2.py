class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf')] * len(triangle[-1]) for _ in range(len(triangle[-1]))] 
        dp[0][0] = triangle[0][0]
        for i in range(len(triangle) - 1):
            for j in range(i+1):
                dp[i+1][j] = min(dp[i][j] + triangle[i+1][j], dp[i+1][j])
                dp[i+1][j+1] = min(dp[i][j] + triangle[i+1][j+1], dp[i+1][j+1])
        return min(dp[-1])