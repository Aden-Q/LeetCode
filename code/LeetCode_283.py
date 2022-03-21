class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        size = len(nums)
        while left < size:
            while left < size and nums[left] != 0:
                left += 1
            # find the first zero entry
            if left >= size:
                break
            right = left + 1
            while right < size and nums[right] == 0:
                right += 1
            # swap left and right
            if right >= size:
                break
            nums[left], nums[right] = nums[right], nums[left]
            # start from the next position
            left += 1