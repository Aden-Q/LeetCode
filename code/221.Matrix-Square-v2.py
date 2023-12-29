class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.max_square = 0

        # returns the maximum square of whose bottom right corner has index (row, col) in the original matrix
        @cache
        def dp(row, col) -> int:
            if row < 0 or col < 0:
                return 0

            ans = min(dp(row-1, col), dp(row, col-1), dp(row-1, col-1))
            
            if matrix[row][col] == '1':
                ans = ans + 1
                self.max_square = max(self.max_square, ans ** 2)
            else:
                ans = 0

            return ans

        dp(m-1, n-1)
        return self.max_square