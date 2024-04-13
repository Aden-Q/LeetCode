class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                cnt += 4
                # Check left, right, up, and bottom
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    cnt -= 1
                if j + 1 < n and grid[i][j+1] == 1:
                    cnt -= 1
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    cnt -= 1
                if i + 1 < m and grid[i+1][j] == 1:
                    cnt -= 1
        
        return cnt