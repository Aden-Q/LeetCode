class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 2D prefix sum
        m, n = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (n+1) for _ in range(m+1)]
        
        for row in range(1,m+1):
            for col in range(1, n+1):
                prefix_sum[row][col] = prefix_sum[row][col-1] + prefix_sum[row-1][col] - prefix_sum[row-1][col-1] + int(matrix[row-1][col-1])
        
        max_square = 0

        # matrix[row1:row2][col1:col2] = prefix_sum[row2][col2] - prefix_sum[row1][col1]
        # a candidate of submatrix must have matrix[row1:row2][col1:col2] == (row2 - row1 + 1) * (col2 - col1 + 1)
        for row in range(m):
            for col in range(n):
                # (row, col) is the index of the upper-left corner
                for length in range(min(m, n)+1):
                    if row + length > m or col + length > n:
                        continue
                    row_end = row +length
                    col_end = col + length
                    if prefix_sum[row + length][col + length] - prefix_sum[row + length][col] - prefix_sum[row][col + length] + prefix_sum[row][col] == length ** 2:
                        max_square = max(max_square, length ** 2)

        return max_square
