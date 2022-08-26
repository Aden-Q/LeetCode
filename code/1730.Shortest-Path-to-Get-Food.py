from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # BFS for sure
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = [[False] * n for _ in range(m)]
        break_flag = False
        # First enque the starting position
        for i in range(m):
            if break_flag:
                break
            for j in range(n):
                if grid[i][j] == '*':
                    q.append((i, j))
                    visited[i][j] = True
                    break_flag = True
                    break
        
        step = -1
        while q:
            sz = len(q)
            step += 1
            for _ in range(sz):
                curr_node = q.popleft()
                curr_x, curr_y = curr_node
                if grid[curr_x][curr_y] == '#':
                    # food cell
                    return step
                
                for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    next_x, next_y = curr_x + d[0], curr_y + d[1]
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    if grid[next_x][next_y] != 'X' and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))
        
        return -1