class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort(key = lambda a : a[0])
        x_len = coordinates[1][0] - coordinates[0][0]
        y_len = coordinates[1][1] - coordinates[0][1]
        cur_x = coordinates[0][0]
        cur_y = coordinates[0][1]
        for i in range(1, len(coordinates)):
            next_x = coordinates[i][0]
            next_y = coordinates[i][1]
            if (next_y - cur_y) * x_len != y_len * (next_x - cur_x):
                return False
            cur_x, cur_y = next_x, next_y
        return True
        