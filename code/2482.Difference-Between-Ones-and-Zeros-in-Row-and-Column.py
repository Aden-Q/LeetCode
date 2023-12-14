class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        # O(mn)
        rowSum = [0 for _ in range(m)]
        for i in range(m):
            rowSum[i] = sum(grid[i][:])

        colSum = [0 for _ in range(n)]
        for j in range(n):
            colSum[j] = sum(1 for i in range(m) if grid[i][j] == 1)

        diff = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * rowSum[i] + 2 * colSum[j] - m - n
        
        return diff
