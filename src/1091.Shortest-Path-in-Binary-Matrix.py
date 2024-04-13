import heapq

class State:
    def __init__(self, x, y, distFromStart):
        self.x = x
        self.y = y
        self.distFromStart = distFromStart
        
    def __lt__(self, other):
        return self.distFromStart < other.distFromStart
        
class Solution:
    def getNeighbours(self, x, y, n, grid):
        res = []
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for d in dirs:
            next_x = x + d[0]
            next_y = y + d[1]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or grid[next_x][next_y] == 1:
                continue
            res.append((next_x, next_y))
        return res

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = 1
        pq = [State(0, 0, dist[0][0])]
        
        while len(pq) != 0:
            cur = heapq.heappop(pq)
            cur_x, cur_y = cur.x, cur.y
            cur_dist = cur.distFromStart
            if cur_x == n-1 and cur_y == n-1:
                return cur_dist
            if cur_dist > dist[cur_x][cur_y]:
                # ignore if the current node is not the candidate for optimal
                continue
            neighbours = self.getNeighbours(cur_x, cur_y, n, grid)
            for neighbour in neighbours:
                next_x, next_y = neighbour[0], neighbour[1]
                if cur_dist + 1 < dist[next_x][next_y]:
                    dist[next_x][next_y] = cur_dist + 1
                    heapq.heappush(pq, State(next_x, next_y, cur_dist + 1))
        return -1