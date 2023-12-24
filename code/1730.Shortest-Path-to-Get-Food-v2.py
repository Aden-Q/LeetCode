class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()

        for row in range(m):
            for col in range(n):
                # first we need to get our location
                if grid[row][col] == '*':
                    queue.append((row, col))

        length = 0
        while queue:
            size = len(queue)
            length += 1

            for _ in range(size):
                curr_row, curr_col = queue.popleft()
                if grid[curr_row][curr_col] == 'X':
                    continue
                    
                # mark as visited
                grid[curr_row][curr_col] = 'X'

                for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    next_row, next_col = curr_row + d[0], curr_col + d[1]
                    if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                        continue
                    if grid[next_row][next_col] == '#':
                        return length
                    if grid[next_row][next_col] == 'O':
                        queue.append((next_row, next_col))
                
        return -1