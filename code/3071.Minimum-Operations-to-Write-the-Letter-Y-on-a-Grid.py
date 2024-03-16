class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counterY = Counter()
        counterNonY = Counter()
        Y_grids = set()
        for i in range(n // 2):
            counterY[grid[i][i]] += 1
            counterY[grid[i][n-1-i]] += 1
            grid[i][i] = -1
            grid[i][n-1-i] = -1

        for i in range(n // 2, n):
            counterY[grid[i][n // 2]] += 1
            grid[i][n // 2] = -1
            
        for row in range(n):
            for col in range(n):
                if grid[row][col] >= 0:
                    counterNonY[grid[row][col]] += 1
        
        sumY = sum(counterY.values())
        sumNonY = sum(counterNonY.values())
        minOps = n * n
        for y in [0, 1, 2]:
            for non_y in [0, 1, 2]:
                if y == non_y:
                    continue
                minOps = min(minOps, n * n - counterY[y] - counterNonY[non_y])
        
        return minOps
