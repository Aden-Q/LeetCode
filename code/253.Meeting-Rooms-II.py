class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        begins = [0] * length
        ends = [0] * length
        
        for i in range(length):
            begins[i] = intervals[i][0]
            ends[i] = intervals[i][1]
            
        begins.sort()
        ends.sort()
        res, i, j = 0, 0, 0
        cnt = 0
        
        while i < length and j < length:
            if begins[i] < ends[j]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1
            res = max(res, cnt)
            
        return res