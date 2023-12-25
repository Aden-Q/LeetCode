class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # this is an edge case
        total_sum = sum(nums)
        if total_sum == 0:
            return 0
        if total_sum == len(nums):
            return total_sum - 1

        max_len = 1
        # count the number of zeros in the subarray
        # we can have at most 1 zero
        cnt_zero = 0
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                cnt_zero += 1
            while left <= right and cnt_zero > 1:
                if nums[left] == 0:
                    cnt_zero -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1 - cnt_zero)
            right += 1

        return max_len
