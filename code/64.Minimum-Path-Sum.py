class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[66666] * n for _ in range(m)]
        
        # represents the minimal score falling to grid[m-1][n-1]
        # starting from grid[i][j]
        def dp(grid, i, j):
            if i == m - 1:
                return sum(grid[i][j:])
            if j == n - 1:
                res = 0
                for row in range(i, m):
                    res += grid[row][j]
                return res
            if memo[i][j] != 66666:
                return memo[i][j]
            memo[i][j] = grid[i][j] + min(dp(grid, i, j+1), dp(grid, i+1, j))
            
            return memo[i][j]
        
        return dp(grid, 0, 0)