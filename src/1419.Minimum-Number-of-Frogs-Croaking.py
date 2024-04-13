from collections import defaultdict
import heapq

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # O(N) time to create the intervals array
        # To count the number of rooms required
        # It takes O(NlogN) time
        # O(N) space: one hash table, one interval array, one priority queue
        def isValid(ht, index):
            if ht['c'][i] < ht['r'][i] and ht['r'][i] < ht['o'][i] and ht['o'][i] < ht['a'][i] and ht['a'][i] < ht['k'][i]:
                return True
            return False
        
        ht = defaultdict(list)
        # Get the indices of each character
        for idx, val in enumerate(croakOfFrogs):
            ht[val].append(idx)
        length = len(ht['c'])
        if len(ht['r']) != length or len(ht['o']) != length or len(ht['a']) != length or len(ht['k']) != length:
            return -1
        intervals = []
        for i in range(length):
            if not isValid(ht, i):
                return -1
            intervals.append((ht['c'][i], ht['k'][i]))
        # intervals are sorted in increasing order by their start time
        pq = [intervals[0][1]]
        
        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            if start > pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, end)
        
        return len(pq)