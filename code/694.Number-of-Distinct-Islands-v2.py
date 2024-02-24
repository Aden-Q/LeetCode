class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        def dfs(row, col, path) -> None:
            nonlocal grid
            
            grid[row][col] = 0
            for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                next_row, next_col = row + d[0], col + d[1]
                if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n or not grid[next_row][next_col]:
                    continue
                path.append(tuple(d))
                dfs(next_row, next_col, path)
                path.append('')

            return

        res = set()
        for row in range(m):
            for col in range(n):
                if not grid[row][col]:
                    # this is not an island
                    continue
                path = []
                dfs(row, col, path)
                res.add(tuple(path))

        return len(res)
