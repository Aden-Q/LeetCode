class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxScore = 0

        def backtrack(row, col, curScore):
            nonlocal maxScore
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            if grid[row][col] == 0:
                return

            oldScore = grid[row][col]
            curScore += oldScore
            maxScore = max(maxScore, curScore)
            grid[row][col] = 0

            backtrack(row+1, col, curScore)
            backtrack(row-1, col, curScore)
            backtrack(row, col+1, curScore)
            backtrack(row, col-1, curScore)

            # backtrack
            grid[row][col] = oldScore

        for row in range(m):
            for col in range(n):
                backtrack(row, col, 0)

        return maxScore
