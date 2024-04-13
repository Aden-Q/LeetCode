class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # multi-source BFS
        m, n = len(rooms), len(rooms[0])

        q = collections.deque()
        # enque all gates
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    q.append((row, col))
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        step = 0
        while q:
            size = len(q)
            step += 1
            for _ in range(size):
                curr_row, curr_col = q.popleft()
                for d in directions:
                    next_row, next_col = curr_row + d[0], curr_col + d[1]
                    if 0 <= next_row < m and 0 <= next_col < n and rooms[next_row][next_col] == 2147483647:
                        rooms[next_row][next_col] = step
                        q.append((next_row, next_col))
        