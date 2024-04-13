class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_row = len(matrix)
        num_col = len(matrix[0])
        zero_first_row = False
        zero_first_col = False
        for i in range(num_col):
            if matrix[0][i] == 0:
                zero_first_row = True
        for i in range(num_row):
            if matrix[i][0] == 0:
                zero_first_col = True
        # move the zeros to the first row and first col
        for i in range(1, num_row):
            for j in range(1, num_col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # update col
        for i in range(1, num_col):
            if matrix[0][i] == 0:
                for j in range(1, num_row):
                    matrix[j][i] = 0
        # update row
        for i in range(1, num_row):
            if matrix[i][0] == 0:
                for j in range(1, num_col):
                    matrix[i][j] = 0
        if zero_first_row == True:
            for i in range(num_col):
                matrix[0][i] = 0
        if zero_first_col == True:
            for i in range(num_row):
                matrix[i][0] = 0