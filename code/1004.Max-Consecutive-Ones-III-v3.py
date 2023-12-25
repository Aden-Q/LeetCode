class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # we can keep a window within which we can have at most k 0's
        left, right = 0, 0
        cnt_zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                cnt_zeros += 1
            if cnt_zeros > k:
                if nums[left] == 0:
                    cnt_zeros -= 1
                left += 1
            
            right += 1

        return right - left