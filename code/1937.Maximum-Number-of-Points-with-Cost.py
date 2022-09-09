class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # O(MN) time, O(N) space
        m, n = len(points), len(points[0])
        dp = points[0][:]
        leftMax = [0] * n
        rightMax = [0] * n
        
        for row in range(1, m):
            leftMax[0] = dp[0]
            rightMax[-1] = dp[-1]
            for col in range(1, n):
                leftMax[col] = max(leftMax[col-1] - 1, dp[col])
            for col in range(n-2, -1, -1):
                rightMax[col] = max(rightMax[col+1] - 1, dp[col])
            for col in range(n):
                dp[col] = max(leftMax[col], rightMax[col]) + points[row][col]
            
        return max(dp)