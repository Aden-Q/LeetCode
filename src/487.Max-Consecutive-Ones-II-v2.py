class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        num_zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeros += 1

            if num_zeros > 1:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            right += 1

        return right - left
