class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    num_fresh += 1
        
        if num_fresh == 0:
            return 0

        step = -1
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                curr_x, curr_y = queue.popleft()
                for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    next_x, next_y = curr_x + d[0], curr_y + d[1]
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    if grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        num_fresh -= 1
                        queue.append((next_x, next_y))
        
        return -1 if num_fresh > 0 else step