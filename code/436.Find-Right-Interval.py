class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # binary search
        intervals_with_index = [[interval, idx] for idx, interval in enumerate(intervals)]
        intervals_with_index.sort(key = lambda x: x[0])
        res = [-1] * n

        for i in range(n):
            curr_interval, curr_interval_idx = intervals_with_index[i]
            # we need to search for the current interval's end time in intervals_with_index
            target = curr_interval[1]
            left, right = i, n
            while left < right:
                mid = left + (right - left) // 2
                if intervals_with_index[mid][0][0] == target:
                    res[curr_interval_idx] = intervals_with_index[mid][1]
                    break
                elif intervals_with_index[mid][0][0] > target:
                    right = mid
                else:
                    left = mid + 1

            if left == right and right < n:
                res[curr_interval_idx] = intervals_with_index[right][1]

        return res
