from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        q = deque()
        q.append([0,0])
        
        def getNeighbours(x, y):
            nonlocal n, dirs
            res = []
            for d in dirs:
                next_x, next_y = x + d[0], y + d[1]
                if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                    continue
                res.append([next_x, next_y])
            return res
        
        dist = 0
        grid[0][0] = 1
        while len(q) != 0:
            sz = len(q)
            dist += 1
            for _ in range(sz):
                cur_x, cur_y = q.popleft()
                if cur_x == n-1 and cur_y == n-1:
                    return dist
                neighbours = getNeighbours(cur_x, cur_y)
                for nbh in neighbours:
                    next_x, next_y = nbh
                    if grid[next_x][next_y] == 0:
                        grid[next_x][next_y] = 1
                        q.append([next_x, next_y])       
        return -1