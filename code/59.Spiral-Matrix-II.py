class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        # corresponding to four directions
        # 0: right
        # 1: down
        # 2: left
        # 3: up
        dir = 0
        row, col = 0, 0
        counter = 0
        while counter < n * n:
            if dir == 0:
                j = col
                while j < n and res[row][j] == 0:
                    counter += 1
                    res[row][j] = counter
                    j += 1
                col = j - 1
                row += 1
                dir = 1
            elif dir == 1:
                j = row
                while j < n and res[j][col] == 0:
                    counter += 1
                    res[j][col] = counter
                    j += 1
                row = j - 1
                col -= 1
                dir = 2
            elif dir == 2:
                j = col
                while j >= 0 and res[row][j] == 0:
                    counter += 1
                    res[row][j] = counter
                    j -= 1
                col = j + 1
                row -= 1
                dir = 3
            elif dir == 3:
                j = row
                while j >= 0 and res[j][col] == 0:
                    counter += 1
                    res[j][col] = counter
                    j -= 1
                row = j + 1
                col += 1
                dir = 0
        return res      