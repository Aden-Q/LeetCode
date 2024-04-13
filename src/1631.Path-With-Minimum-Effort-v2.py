class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        differenceMatrix = [[float('inf')] * n for _ in range(m)]
        # pairs of: (cost, row, col)
        pq = [(0, 0 , 0)]

        # run dijkstra
        while pq:
            cost, curr_row, curr_col = heapq.heappop(pq)
            if (curr_row, curr_col) == (m-1, n-1):
                # the first time we see (m-1, n-1), we get the answer
                return cost
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                next_row, next_col = curr_row + dx, curr_col + dy
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                    continue
                curr_cost = max(abs(heights[next_row][next_col] - heights[curr_row][curr_col]), cost)
                if curr_cost < differenceMatrix[next_row][next_col]:
                    differenceMatrix[next_row][next_col] = curr_cost
                    heapq.heappush(pq, (curr_cost, next_row, next_col))
