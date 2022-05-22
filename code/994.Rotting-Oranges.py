from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = -1
        q = deque()
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
        if len(q) == 0:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return -1
            return 0
        while len(q) != 0:
            sz = len(q)
            count += 1
            for _ in range(sz):
                cur_x, cur_y = q.popleft()
                for d in dirs:
                    next_x, next_y = cur_x + d[0], cur_y + d[1]
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or grid[next_x][next_y] != 1:
                        continue
                    grid[next_x][next_y] = 2
                    q.append([next_x, next_y])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return count