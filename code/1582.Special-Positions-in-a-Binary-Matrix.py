class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        rowSum = [0 for _ in range(m)]
        for i in range(m):
            rowSum[i] = sum(1 for j in range(n) if mat[i][j] == 1)
        
        colSum = [0 for _ in range(n)]
        for j in range(n):
            colSum[j] = sum(1 for i in range(m) if mat[i][j] == 1)

        res = 0
        for i in range(m):
            for j in range(n):
                res += (mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1)

        return res
