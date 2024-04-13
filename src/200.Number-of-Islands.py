class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row, col = len(grid), len(grid[0])
        
        def dfs(i, j):
            nonlocal grid, row, col
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            return

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count