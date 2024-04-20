class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []

        # traverse from top to bottom, left to right
        def dfs(row, col, maxRow, maxCol) -> (int, int):
            if row >= m or col >= n:
                return maxRow, maxCol

            if land[row][col] == 0:
                return maxRow, maxCol

            land[row][col] = 0
            maxRow = max(maxRow, row)
            maxCol = max(maxCol, col)

            for d in [[1, 0], [0, 1]]:
                next_row, next_col = row + d[0], col + d[1]
                maxRowNext, maxColNext = dfs(next_row, next_col, maxRow, maxCol)
                maxRow = max(maxRow, maxRowNext)
                maxCol = max(maxCol, maxColNext)
            
            return maxRow, maxCol

        for row in range(m):
            for col in range(n):
                if land[row][col] == 1:
                    maxRow, maxCol = dfs(row, col, row, col)
                    res.append([row, col, maxRow, maxCol])

        return res
