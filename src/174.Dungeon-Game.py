class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        memo = [[-1] * n for _ in range(m)]
        
        # dp[i][j] represents the minial health needed
        # to reach the target starting from (i, j)
        def dp(dungeon, i, j):
            if i == m - 1 and j == n - 1:
                if dungeon[i][j] > 0:
                    return 1
                return -dungeon[i][j] + 1
            if i == m or j == n:
                return 66666666666
            
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = min(dp(dungeon, i, j+1), dp(dungeon, i+1, j)) - dungeon[i][j]
            memo[i][j] = max(1, memo[i][j])
            
            return memo[i][j]
        
        return dp(dungeon, 0, 0)