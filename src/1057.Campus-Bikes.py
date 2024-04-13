class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n, m = len(workers), len(bikes)
        res = [0] * n
        # we need to calculate the distances between every pair of (worker, bike) and use a min heap to store it
        # we use the (worker index, bike index) as the tie breaker
        worker_used = set()
        bike_used = set()

        pq = []
        for worker_idx in range(n):
            for bike_idx in range(m):
                worker_x, worker_y = workers[worker_idx]
                bike_x, bike_y = bikes[bike_idx]
                manhattan_dist = abs(worker_x - bike_x) + abs(worker_y - bike_y) 
                heapq.heappush(pq, (manhattan_dist, worker_idx, bike_idx))

        while len(worker_used) != n:
            manhattan_dist, worker_idx, bike_idx = heapq.heappop(pq)
            if worker_idx in worker_used or bike_idx in bike_used:
                continue
            
            res[worker_idx] = bike_idx
            worker_used.add(worker_idx)
            bike_used.add(bike_idx)

        return res
