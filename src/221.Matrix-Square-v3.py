class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_square = 0

        dp = [[0] * (n+1) for _ in range(m+1)]
        for row in range(1, m+1):
            for col in range(1, n+1):
                if matrix[row-1][col-1] == '1':
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                    max_square = max(max_square, dp[row][col] ** 2)

        return max_square