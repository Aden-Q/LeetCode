from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Construct a nxn graph from the input
        # It is a directional weighted graph
        # 0 is an invalid price
        graph = [[0] * n for _ in range(n)]
        for flight in flights:
            first, second, price = flight
            graph[first][second] = price
        
        # Run BFS, at most k + 1 steps
        q = deque([(src, 0)])
        # global var, current minimal price to travel from src to dst
        curr_min = float('inf')
        dist = defaultdict(float)
        dist[src] = 0
        dist[dst] = float('inf')
        
        while q and k >= -1:
            sz = len(q)
            # One step
            k -= 1
            for _ in range(sz):
                curr_city, curr_price = q.popleft()
                if curr_city == dst:
                    # reachable from the current city
                    # Update the global var
                    curr_min = min(curr_min, curr_price)
                # Check all the neighbors
                for next_city in range(n):
                    if graph[curr_city][next_city] != 0 and dist.get(next_city, float('inf')) > curr_price + graph[curr_city][next_city]:
                        q.append((next_city, curr_price + graph[curr_city][next_city]))
                        # Update this distance from the source
                        dist[next_city] = curr_price + graph[curr_city][next_city]
        
        if curr_min == float('inf'):
            return -1
        return curr_min