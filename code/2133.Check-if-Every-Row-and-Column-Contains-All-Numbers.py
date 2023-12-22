class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for row in range(n):
            # check every row
            digits = set(range(1, n+1))
            for col in range(n):
                digits.discard(matrix[row][col])
            # check if we've seen all digits [1...n] inclusive
            if len(digits) != 0:
                return False

        for col in range(n):
            # check every column
            digits = set(range(1, n+1))
            for row in range(n):
                digits.discard(matrix[row][col])
             # check if we've seen all digits [1...n] inclusive
            if len(digits) != 0:
                return False

        return True