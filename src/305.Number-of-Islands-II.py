class UF:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y) -> None:
        root_x, root_y = self.find(x), self.find(y)
        self.parent[root_x] = self.parent[root_y]
        
        return

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def convertToIndx(row, col):
            return row * n + col

        grid = [[0] * n for _ in range(m)]
        uf = UF(m * n)
        count_islands = 0
        res = []
        for row, col in positions:
            # this is when the position is duplicated
            if grid[row][col] == 1:
                res.append(count_islands)
                continue
            count_islands += 1
            grid[row][col] = 1
            for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                next_row, next_col = row + d[0], col + d[1]
                if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n or not grid[next_row][next_col]:
                    continue
                idx, next_idx = convertToIndx(row, col), convertToIndx(next_row, next_col)
                if uf.connected(idx, next_idx):
                    continue
                else:
                    uf.union(idx, next_idx)
                    count_islands -= 1
            
            res.append(count_islands)

        return res
