class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0),
        }

        curr = (0, 0)
        visited = set([curr])
        for d in path:
            d_vec = directions[d]
            curr = (curr[0] + d_vec[0], curr[1] + d_vec[1])
            if curr in visited:
                return True
            visited.add(curr)
        
        return False