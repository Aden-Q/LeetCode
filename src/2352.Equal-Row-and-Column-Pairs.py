class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counter = Counter()
        res = 0

        for row in grid:
            counter[tuple(row)] += 1

        for col_idx in range(n):
            col = [grid[r][col_idx] for r in range(n)]
            res += counter[tuple(col)]

        return res
