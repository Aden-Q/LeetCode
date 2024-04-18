class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        old_color = grid[row][col]
        res = copy.deepcopy(grid)
        visited = set()

        def dfs(r, c) -> None:
            nonlocal res, color, m, n

            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if grid[r][c] != old_color:
                return

            if (r, c) in visited:
                return

            visited.add((r, c))
            
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                res[r][c] = color
            elif grid[r-1][c] != old_color or grid[r+1][c] != old_color or grid[r][c-1] != old_color or grid[r][c+1] != old_color:
                res[r][c] = color
            
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

            return

        dfs(row, col)
        return res
