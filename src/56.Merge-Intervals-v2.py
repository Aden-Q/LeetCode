class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x : x[0])
        curr_start, curr_end = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= curr_end:
                curr_end = max(curr_end, intervals[i][1])
            else:
                res.append([curr_start, curr_end])
                curr_start, curr_end = intervals[i][0], intervals[i][1]
        
        res.append([curr_start, curr_end])
        
        return res