class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def validCoord(row, col):
            return 0 <= row < m and 0 <= col < n

        @cache
        def dfs(row, col):
            if not validCoord(row, col):
                return 0
            if row == 0:
                return 1
            if col == 0:
                return 1
            
            return dfs(row-1, col) + dfs(row, col-1)

        return dfs(m-1, n-1)
         