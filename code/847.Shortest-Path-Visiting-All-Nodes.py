from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # we have nodes labeled 0 ~ n - 1
        n = len(graph)
        # ith bit of mask represents the 
        # visiting status of node i (0-indexed)
        mask = 1 << n
        # (mask, n): mask is the visiting status of the graph, n is the last visited node
        dist = [[float('inf')] * n for _ in range(mask)]
        q = deque()
        # enque starting points for bfs
        for i in range(n):
            dist[1 << i][i] = 0
            q.append((1 << i, i))
        
        # bfs
        while len(q) != 0:
            state, cur_node = q.popleft()
            step = dist[state][cur_node]
            # terminate state (when all nodes are visited for the first time)
            if state == mask - 1:
                return  step
            # enque neighbours
            for ngb in graph[cur_node]:
                if dist[state | 1 << ngb][ngb] > step + 1:
                    # update distance
                    dist[state | 1 << ngb][ngb] = step + 1
                    # enque
                    q.append((state | 1 << ngb, ngb))
        # Hamiltonian path does not exist, won't reach this statement
        return -1