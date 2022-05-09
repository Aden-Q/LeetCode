class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        # start from the first row
        for i in range(col):
            j = 1
            while j < row and i + j < col:
                if matrix[j][i+j] != matrix[j-1][i+j-1]:
                    return False
                j += 1
        for i in range(row):
            j = 1
            while i+j < row and j < col:
                if matrix[i+j][j] != matrix[i+j-1][j-1]:
                    return False
                j += 1
        
        return True