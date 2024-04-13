from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sl = SortedList()
        right = 0
        minAbsDiff = inf
        for idx, num in enumerate(nums):
            if idx - right >= x:
                sl.add(nums[right])
                right += 1
            
            if len(sl) > 0:
                idx = sl.bisect_right(num)
                if idx < len(sl):
                    minAbsDiff = min(minAbsDiff, abs(num - sl[idx]))
                if idx - 1 >= 0:
                    minAbsDiff = min(minAbsDiff, abs(num - sl[idx-1]))

        return minAbsDiff
