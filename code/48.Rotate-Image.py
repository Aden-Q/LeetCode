class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 对角线对称
        num_row = len(matrix)
        num_col = len(matrix[0])
        for i in range(num_row):
            for j in range(i, num_col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 列对称
        for i in range(num_row):
            for j in range(num_col // 2):
                matrix[i][j], matrix[i][num_col-1-j] = matrix[i][num_col-1-j], matrix[i][j]
        return matrix