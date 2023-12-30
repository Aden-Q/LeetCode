class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num_grid = m * n
        start_row, start_col = 0, 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == -1:
                    num_grid -= 1
                elif grid[row][col] == 1:
                    start_row, start_col = row, col

        # we need to visit num_grid and end at the ending square in order for a path to be counted
        count = 0
        def dfs(row, col, num) -> None:
            nonlocal count, grid
            num -= 1
            if grid[row][col] == 2:
                if num == 0:
                    # at ending square and we've visited all grids once
                    count += 1
                return
            
            tmp_val = grid[row][col]
            grid[row][col] = -1
            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row, next_col = row + d[0], col + d[1]
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                    continue
                if grid[next_row][next_col] == -1:
                    # we don't step into an obstacle
                    continue
                dfs(next_row, next_col, num)
            
            grid[row][col] = tmp_val
            return

        dfs(start_row, start_col, num_grid)
        return count
