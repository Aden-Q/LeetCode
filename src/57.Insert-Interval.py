class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        res = []
        new_left, new_right = newInterval

        flag = False
        for i in range(len(intervals)):
            interval = intervals[i]
            # check overlap or not
            left, right = interval
            if right < new_left:
                # non-overlapping, continue
                res.append(interval)
                continue
            if left > new_right:
                # end of merging, we can break
                res.append([new_left, new_right])
                res.extend(intervals[i:])
                flag = True
                break
                
            # overlapping, calculate new interval endpoints
            new_left = min(new_left, left)
            new_right = max(new_right, right)

        if not flag:
            res.append([new_left, new_right])
        return res
