class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # greedy, it's best to remove the numbers that have the least occurance
        # we can build a priority queue, sorted by occurance
        counter = Counter(arr)
        pq = [val for val in counter.values()]
        heapq.heapify(pq)
    
        while pq and k > 0:
            if pq[0] <= k:
                k -= heapq.heappop(pq)
            else:
                break

        return len(pq)
