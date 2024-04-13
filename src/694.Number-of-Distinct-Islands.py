class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        def dfs(row, col, path) -> None:
            nonlocal grid
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            if not grid[row][col]:
                return
            
            path.append((row, col))
            grid[row][col] = 0
            for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                next_row, next_col = row + d[0], col + d[1]
                dfs(next_row, next_col, path)

            return

        def addToSet(res, path):
            row_min, col_min = min(p[0] for p in path), min(p[1] for p in path)
            path = [(p[0] - row_min, p[1] - col_min) for p in path]
            res.add(tuple(path))

            return

        res = set()
        for row in range(m):
            for col in range(n):
                if not grid[row][col]:
                    # this is not an island
                    continue
                path = []
                dfs(row, col, path)
                addToSet(res, path)

        return len(res)
