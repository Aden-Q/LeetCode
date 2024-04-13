class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        # First brute force approach
        res = [[0] * col for _ in range(row)]
        
        for i in range(row):
            # Count from left
            prefix_sum = 0
            for j in range(col):
                if grid[i][j] == 'W':
                    # Reset prefix sum
                    prefix_sum = 0
                elif grid[i][j] == 'E':
                    # This enemy can be killed
                    prefix_sum += 1
                else:
                    res[i][j] += prefix_sum
            # Count from right
            prefix_sum = 0
            for j in range(col-1, -1, -1):
                if grid[i][j] == 'W':
                    # Reset prefix sum
                    prefix_sum = 0
                elif grid[i][j] == 'E':
                    # This enemy can be killed
                    prefix_sum += 1
                else:
                    res[i][j] += prefix_sum
                    
        for j in range(col):
            # Count from top
            prefix_sum = 0
            for i in range(row):
                if grid[i][j] == 'W':
                    # Reset prefix sum
                    prefix_sum = 0
                elif grid[i][j] == 'E':
                    # This enemy can be killed
                    prefix_sum += 1
                else:
                    res[i][j] += prefix_sum
            # Count from bottom
            prefix_sum = 0
            for i in range(row-1, -1, -1):
                if grid[i][j] == 'W':
                    # Reset prefix sum
                    prefix_sum = 0
                elif grid[i][j] == 'E':
                    # This enemy can be killed
                    prefix_sum += 1
                else:
                    res[i][j] += prefix_sum
        
        max_val = 0
        for i in range(row):
            row_max = max(res[i])
            max_val = max(max_val, row_max)
            
        return max_val