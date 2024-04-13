class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # O(N) space
        prev_row = grid[0][:]
        curr_row = [0] * n
        prev_row_min_tuple, prev_row_second_min_tuple = (-1, math.inf), (-1, math.inf)
        for col in range(n):
            if prev_row[col] < prev_row_min_tuple[1]:
                prev_row_min_tuple, prev_row_second_min_tuple = (col, prev_row[col]), prev_row_min_tuple
            elif prev_row[col] < prev_row_second_min_tuple[1]:
                prev_row_second_min_tuple = (col, prev_row[col])

        for row in range(1, n):
            curr_row_min_tuple, curr_row_second_min_tuple = (-1, math.inf), (-1, math.inf)
            for col in range(n):
                if prev_row_min_tuple[0] == col:
                    # we should use the second min to update
                    curr_row[col] = prev_row[prev_row_second_min_tuple[0]] + grid[row][col]
                else:
                    # we should use row min to update
                    curr_row[col] = prev_row[prev_row_min_tuple[0]] + grid[row][col]
                # update current row min and current row second min
                if curr_row[col] < curr_row_min_tuple[1]:
                    curr_row_min_tuple, curr_row_second_min_tuple = (col, curr_row[col]), curr_row_min_tuple
                elif curr_row[col] < curr_row_second_min_tuple[1]:
                    curr_row_second_min_tuple = (col, curr_row[col])
            
            prev_row, curr_row = curr_row, prev_row
            prev_row_min_tuple, prev_row_second_min_tuple = curr_row_min_tuple, curr_row_second_min_tuple

        return min(prev_row)
