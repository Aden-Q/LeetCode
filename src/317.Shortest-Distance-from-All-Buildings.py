class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # multi source BFS, starting from all buildings, we search for the first grid visited by all buildings
        m, n = len(grid), len(grid[0])
        q = deque()
        # a dictionary keeping track of which buildings have visited a grid
        visited = defaultdict(set)

        building_idx = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    q.append((row, col, building_idx))
                    building_idx += 1

        # when running BFS, we need to make sure the same node is visited by the same building twice
        # each member in the q is a tuple, the first two elements represent the current position, the last two elements
        # represent the source of the traffic (a building), so we allow the same grid to be enque multiple times
        # but does not allow the same 4-tuple to be enqued
        step = 0
        res = []
        canBeVisited = False
        while q:
            step += 1
            size = len(q)
            for _ in range(size):
                curr_row, curr_col, idx = q.popleft()
                # visit its neighbors
                for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row, next_col = curr_row + d[0], curr_col + d[1]
                    if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or grid[next_row][next_col] > 0:
                        continue
                    if (next_row, next_col) in visited and idx in visited[(next_row, next_col)]:
                        continue
                    # otherwise we should visit this node from the source
                    visited[(next_row, next_col)].add(idx)
                    grid[next_row][next_col] -= step
                    if len(visited[(next_row, next_col)]) == building_idx:
                        canBeVisited = True
                        res.append(-grid[next_row][next_col])
                    q.append((next_row, next_col, idx))

        return min(res) if canBeVisited else -1
