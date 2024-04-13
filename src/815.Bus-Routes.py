class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # we can build a graph, connectivity can be defined as:
        # if two buses share at least one same stop, then they are connected
        # to test connectivity and membership efficiently, we first convert all lists to sets
        buses = [set(route) for route in routes]
        # the total number of buses
        n = len(routes)
        q = deque()
        # keep track of all buses that has been visited so far
        visited = set()
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if len(buses[i].intersection(buses[j])) != 0:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # populate the initial queue
        for i in range(n):
            if source in buses[i]:
                q.append(i)
                # mark bus i as visited
                visited.add(i)

        # run bfs
        step = 0
        while q:
            step += 1
            sz = len(q)
            for _ in range(sz):
                curr_bus_idx = q.popleft()
                if target in buses[curr_bus_idx]:
                    return step
                # visit the next bus
                for next_bus_idx in graph[curr_bus_idx]:
                    if next_bus_idx in visited:
                        continue
                    q.append(next_bus_idx)
                    visited.add(next_bus_idx)

        # if we visit all buses and cannot find the target, then return -1
        return -1
