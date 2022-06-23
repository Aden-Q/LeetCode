class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            nonlocal grid, m, n
            if grid[r][c] == '1':
                grid[r][c] = '0'
                if r - 1 > -1:
                    dfs(r-1, c)
                if r + 1 < m:
                    dfs(r+1, c)
                if c - 1 > -1:
                    dfs(r, c-1)
                if c + 1 < n:
                    dfs(r, c+1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count