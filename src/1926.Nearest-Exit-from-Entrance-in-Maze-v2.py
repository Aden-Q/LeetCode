class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        steps = -1
        start_row, start_col = entrance
        queue = deque([(start_row, start_col, 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_x, curr_y, step = queue.popleft()
                for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    next_x, next_y = curr_x + d[0], curr_y + d[1]
                    if 0 <= next_x < m and 0 <= next_y < n and maze[next_x][next_y] != '+':
                        if (next_x == 0 or next_x == m - 1 or next_y == 0 or next_y == n-1) and [next_x, next_y] != entrance:
                            return step + 1

                        maze[next_x][next_y] = '+'
                        queue.append((next_x, next_y, step+1))
            
        return -1
