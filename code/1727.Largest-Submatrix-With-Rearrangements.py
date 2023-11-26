class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        currMax = 0
        m = len(matrix)
        n = len(matrix[0])
        countOnes = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            countOnes[m-1][j] = matrix[m-1][j] 

        for j in range(n):
            for i in range(m-2, -1, -1):
                if matrix[i][j] == 1:
                    countOnes[i][j] = countOnes[i+1][j] + 1
        
        for i in range(m):
            row = sorted(countOnes[i], reverse=True)
            for j in range(n):
                currMax = max(currMax, row[j] * (j + 1))

        return currMax