class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                for i in range(k):
                    res[row][col] += mat1[row][i] * mat2[i][col]
        
        return res
