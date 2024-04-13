class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # return the length of the longest increasing sequence starting from grid matrix[row][col] 
        @cache
        def dp(row, col):
            max_len = 1

            for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + d[0], col + d[1]
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                    continue
                if matrix[next_row][next_col] <= matrix[row][col]:
                    continue
                max_len = max(max_len, dp(next_row, next_col) + 1)

            return max_len

        max_len = 1
        for row in range(m):
            for col in range(n):
                max_len = max(max_len, dp(row, col))
        
        return max_len