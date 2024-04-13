class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
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
            
            max_len = max(max_len, right - left)
            right += 1

        return max_len
