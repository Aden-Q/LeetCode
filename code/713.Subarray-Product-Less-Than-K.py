class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        res = 0
        prod = 1
        left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:  # narrow the window size
                prod //= nums[left]
                left += 1
            # accumulate all subarrays with right end equals nums[right]
            res += right - left + 1
        return res