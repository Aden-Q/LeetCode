class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        cur_end = intervals[0][1]
        cnt = 0
        
        for interval in intervals[1:]:
            start, end = interval
            if start >= cur_end:
                # Update the current interval
                cur_end = end
            else:
                # Otherwise delete this interval from the list
                cnt += 1
        
        return cnt