import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # If there is only one or no meetings, then return true for sure
        if len(intervals) <= 1:
            return True
        # Sort by the start timei
        heapq.heapify(intervals)
        
        prev = intervals[0]
        while len(intervals) > 1:
            heapq.heappop(intervals)
            cur = intervals[0]
            if cur[0] < prev[1]:
                return False
            prev = cur
        
        return True