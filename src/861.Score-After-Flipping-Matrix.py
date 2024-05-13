class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        # first greedy flip rows
        for row in range(m):
            if grid[row][0] == 0:
                # flip this row
                for col in range(n):
                    grid[row][col] = 1 - grid[row][col]

        # then greedy flip columns, instead of flip, calculate the decimal gain directly
        for col in range(n):
            num_ones = 0
            for row in range(m):
                if grid[row][col] == 1:
                    num_ones += 1
            
            res += pow(2, n - 1 - col) * max(num_ones, m - num_ones)

        return res
