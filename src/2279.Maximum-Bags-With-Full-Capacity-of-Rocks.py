import heapq

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        num_valid = 0
        pq = []
        for i in range(len(capacity)):
            num = capacity[i] - rocks[i]
            if num == 0:
                num_valid += 1
            else:
                heapq.heappush(pq, num)
                
        while additionalRocks > 0 and len(pq) > 0:
            cur = heapq.heappop(pq)
            if additionalRocks >= cur:
                num_valid += 1
            additionalRocks -= cur
        return num_valid