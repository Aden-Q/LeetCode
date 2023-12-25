class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # we can keep a window within which we can have at most k 0's
        left, right = 0, 0
        cnt_zeros = 0
        max_len = 0

        while right < len(nums):
            if nums[right] == 0:
                cnt_zeros += 1
            while left <= right and cnt_zeros > k:
                if nums[left] == 0:
                    cnt_zeros -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len