from sortedcontainers import SortedList

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList([0])
        prefixSum = 0
        ans = 0
        for num in nums:
            prefixSum += num
            # we need to find lower <= prefixSum - prevSum <= upper
            # which means we need to search for prefixSum - upper <= prevSum <= prefixSum - lower
            left_boundary = sl.bisect_left(prefixSum-upper)
            right_boundary = sl.bisect_right(prefixSum-lower)
            ans += max(0, right_boundary - left_boundary)
            sl.add(prefixSum)

        return ans
