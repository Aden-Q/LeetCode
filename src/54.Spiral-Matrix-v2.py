class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = -101
        res = []
        m, n = len(matrix), len(matrix[0])

        row, col = 0, 0
        while len(res) < m * n:
            # go right
            while col < n and matrix[row][col] != visited:
                res.append(matrix[row][col])
                matrix[row][col] = visited
                col += 1
            # go bottom
            col -= 1
            row += 1
            while row < m and matrix[row][col] != visited:
                res.append(matrix[row][col])
                matrix[row][col] = visited
                row += 1
            # go left
            row -= 1
            col -= 1
            while col >= 0 and matrix[row][col] != visited:
                res.append(matrix[row][col])
                matrix[row][col] = visited
                col -= 1
            # go up
            col += 1
            row -= 1
            while row >= 0 and matrix[row][col] != visited:
                res.append(matrix[row][col])
                matrix[row][col] = visited
                row -= 1
            row += 1
            col += 1
        
        return res