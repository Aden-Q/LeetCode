from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dist = [[0] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i, j])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while len(q) != 0:
            sz = len(q)
            for _ in range(sz):
                cur_x, cur_y = q.popleft()
                for d in dirs:
                    next_x, next_y = cur_x + d[0], cur_y + d[1]
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >=n:
                        continue
                    if mat[next_x][next_y] == 1:
                        dist[next_x][next_y] = dist[cur_x][cur_y] + 1
                        mat[next_x][next_y] = 0
                        q.append([next_x, next_y])
        return dist