import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # O(NlogN) where N is the number of intervals
        # O(N) space for the priority queue
        intervals.sort(key = lambda x : x[0])
        # We need at least allocate a meeting room for the first meeting
        pq = []
        heapq.heappush(pq, intervals[0][1])
        
        for start_time, end_time in intervals[1:]:
            if start_time >= pq[0]:
                # The new meeting can use this room after the meeting in this room ends
                heapq.heappop(pq)
            heapq.heappush(pq, end_time)
        
        return len(pq)    