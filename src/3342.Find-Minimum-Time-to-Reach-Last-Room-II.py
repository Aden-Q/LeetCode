class State:
    def __init__(self, x, y, dist, flag):
        self.x = x
        self.y = y
        self.dist = dist
        # a flag to indicate whether it takes one second or two seconds for the next move from this position
        self.flag = flag

    def __lt__(self, other) -> bool:
        return self.dist < other.dist


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[inf] * m for _ in range(n)]
        dist[0][0] = 0
        visited = [[False] * m for _ in range(n)]

        pq = []
        heapq.heappush(pq, State(0, 0, 0, True))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while pq:
            curr = heapq.heappop(pq)
            if curr.x == n - 1 and curr.y == m - 1:
                return curr.dist

            if visited[curr.x][curr.y]:
                continue

            visited[curr.x][curr.y] = True

            for d in directions:
                next_x, next_y = curr.x + d[0], curr.y + d[1]
                if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                    continue
                next_dist = max(moveTime[next_x][next_y], dist[curr.x][curr.y]) + (
                    1 if curr.flag else 2
                )

                if dist[next_x][next_y] > next_dist:
                    dist[next_x][next_y] = next_dist
                    heapq.heappush(pq, State(next_x, next_y, next_dist, not curr.flag))

        return dist[n - 1][m - 1]
