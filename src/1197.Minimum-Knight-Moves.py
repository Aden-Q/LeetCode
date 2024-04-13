from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        steps = -1
        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        
        while len(q) != 0:
            sz = len(q)
            steps += 1
            for _ in range(sz):
                cur_x, cur_y = q.popleft()
                if (cur_x, cur_y) == (x, y):
                    return steps
                for next_dir in dirs:
                    next_x, next_y = cur_x + next_dir[0], cur_y + next_dir[1]
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y))
        return 0
                