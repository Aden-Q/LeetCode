class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(N) greedy approach, where N is the length of intervals
        intervals.sort(key = lambda x : x[0])
        cur_end = intervals[0][1]
        cnt = 0
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= cur_end:
                # Add this interval
                cur_end = end
            else:
                # Remove this interval
                cnt += 1
                cur_end = min(cur_end, end)
                
        return cnt