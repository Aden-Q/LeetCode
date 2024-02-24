class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # divided and conquer
        m, n = len(matrix), len(matrix[0])

        # search a row in the origial matrix for target, return True if found
        def searchRow(row_idx) -> bool:
            idx = bisect.bisect_left(matrix[row_idx], target)
            if idx >= n or matrix[row_idx][idx] != target:
                return False
            
            return True

        for row_idx in range(m):
            if searchRow(row_idx):
                return True
        
        return False
