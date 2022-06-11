class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        running_sum = 0
        left = 0
        res = 0
        for right, val in enumerate(nums):
            running_sum += nums[right]
            while running_sum * (right - left + 1) >= k:
                # narrow down the window
                running_sum -= nums[left]
                left += 1
            res += right - left + 1
        return res