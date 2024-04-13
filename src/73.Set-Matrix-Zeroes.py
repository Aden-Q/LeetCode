class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_row = len(matrix)
        num_col = len(matrix[0])
        zero_rows = [0] * num_row
        zero_cols = [0] * num_col
        for i in range(num_row):
            for j in range(num_col):
                if matrix[i][j] == 0:
                    zero_rows[i] = 1
                    zero_cols[j] = 1
        for i in range(num_row):
            for j in range(num_col):
                if zero_rows[i] == 1 or zero_cols[j] == 1:
                    matrix[i][j] = 0