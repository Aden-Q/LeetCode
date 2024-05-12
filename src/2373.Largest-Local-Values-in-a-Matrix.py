class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n-2) for _ in range(n-2)]

        def getMax(row_start, row_end, col_start, col_end) -> int:
            maxVal = -inf
            for row in range(row_start, row_end+1):
                for col in range(col_start, col_end+1):
                    maxVal = max(maxVal, grid[row][col])

            return maxVal

        for row in range(n-2):
            for col in range(n-2):
                maxLocal[row][col] = getMax(row, row+2, col, col+2)

        return maxLocal
