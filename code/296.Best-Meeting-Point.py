class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_coordinates = []
        col_coordinates = []
        points = []

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    row_coordinates.append(row)
                    col_coordinates.append(col)
                    points.append((row, col))

        row_coordinates.sort()
        col_coordinates.sort()
        optimal_row = row_coordinates[len(row_coordinates) // 2]
        optimal_col = col_coordinates[len(col_coordinates) // 2]
        res = 0
        for point in points:
            point_row, point_col = point
            res += abs(point_row - optimal_row) + abs(point_col - optimal_col)

        return res
                