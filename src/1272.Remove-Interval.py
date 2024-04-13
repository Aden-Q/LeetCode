class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
                res.append(interval)
            else:
                if interval[0] < toBeRemoved[0]:
                    res.append([interval[0], toBeRemoved[0]])
                if interval[1] > toBeRemoved[1]:
                    res.append([toBeRemoved[1], interval[1]])
            
        return res
