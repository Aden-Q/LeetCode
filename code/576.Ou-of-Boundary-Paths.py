class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7
        def isOutOfBoundary(row, col) -> bool:
            if row < 0 or row >= m:
                return True
            
            if col < 0 or col >= n:
                return True

            return False

        # return the number of paths to move the ball out of the grid boundary starting at (row, col) with numMove remained
        @cache
        def dp(row, col, numMove) -> int:
            if numMove < 0:
                return 0

            if isOutOfBoundary(row, col):
                return 1

            res = dp(row-1, col, numMove-1)
            res = (res + dp(row+1, col, numMove-1)) % mod
            res = (res + dp(row, col-1, numMove-1)) % mod
            res = (res + dp(row, col+1, numMove-1)) % mod

            return res

        return dp(startRow, startColumn, maxMove)
