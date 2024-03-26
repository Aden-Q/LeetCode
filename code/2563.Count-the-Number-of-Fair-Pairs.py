from sortedcontainers import SortedList

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        # lower - nums[j] <= nums[i] <= upper - nums[j]
        sl = SortedList()
        ans = 0
        for num in nums:
            start_idx = sl.bisect_left(lower - num)
            end_idx = sl.bisect_right(upper - num)
            # [start_idx, end_idx) satisfies the condition
            ans += end_idx - start_idx
            sl.add(num)
        
        return ans
