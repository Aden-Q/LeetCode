class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        safeness_grid = [[inf] * n for _ in range(n)]

        # a shortcut
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        # the first thing to do is calculating safeness for all grids
        thieves = deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    thieves.append((row, col))
                    safeness_grid[row][col] = 0

        # multi-source BFS to creat a safeness board
        while thieves:
            size = len(thieves)
            for _ in range(size):
                cur_row, cur_col = thieves.popleft()
                for d in [[0,1], [0, -1], [1, 0], [-1, 0]]:
                    next_row, next_col = cur_row + d[0], cur_col + d[1]
                    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                        continue
                    if safeness_grid[next_row][next_col] <= safeness_grid[cur_row][cur_col] + 1:
                        continue
                    safeness_grid[next_row][next_col] = safeness_grid[cur_row][cur_col] + 1
                    thieves.append((next_row, next_col))

        # priority queue to get the optimal score to reach the target
        pq = [[-safeness_grid[0][0], 0, 0]]
        safeness_grid[0][0] = 0

        while pq:
            safeness, row, col = heapq.heappop(pq)
            if (row, col) == (n-1, n-1):
                return -safeness
            for d in [[0,1], [0, -1], [1, 0], [-1, 0]]:
                next_row, next_col = row + d[0], col + d[1]
                if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                    continue
                if safeness_grid[next_row][next_col] == 0:
                    continue
                heapq.heappush(pq, [-min(-safeness, safeness_grid[next_row][next_col]), next_row, next_col])
                safeness_grid[next_row][next_col] = 0

        return 0
