class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # visit/sink all 1's from the starting point
        def dfs(grid, row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            if grid[row][col] == 0:
                return

            grid[row][col] = 0
            dfs(grid, row-1, col)
            dfs(grid, row+1, col)
            dfs(grid, row, col-1)
            dfs(grid, row, col+1)

            return

         # count the number of islands for the given grid
        def countNumIslands(grid) -> int:
            cnt = 0
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 1:
                        cnt += 1
                        dfs(grid, row, col)

            return cnt

        if countNumIslands(copy.deepcopy(grid)) != 1:
            return 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                
                grid_copy = copy.deepcopy(grid)
                grid_copy[row][col] = 0
                if countNumIslands(grid_copy) != 1:
                    return 1
        
        return 2
