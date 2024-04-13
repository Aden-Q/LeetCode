class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dir_maps = {
            'L': [0, -1],
            'R': [0, 1],
            'U': [-1, 0],
            'D': [1, 0],
        }
    
        def dfs(row, col, path) -> None:
            nonlocal grid
            
            grid[row][col] = 0
            for d in 'LRUD':
                next_row, next_col = row + dir_maps[d][0], col + dir_maps[d][1]
                if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n or not grid[next_row][next_col]:
                    continue
                path.append(d)
                dfs(next_row, next_col, path)
                path.append(' ')

            return

        res = set()
        for row in range(m):
            for col in range(n):
                if not grid[row][col]:
                    # this is not an island
                    continue
                path = []
                dfs(row, col, path)
                res.add(''.join(path))

        return len(res)
