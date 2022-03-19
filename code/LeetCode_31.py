class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 1
        while idx > 0:
            if nums[idx-1] < nums[idx]:
                break
            idx -= 1
        if idx == 0:
            nums.reverse()
            return
        j = idx
        while j <= len(nums) - 1 and nums[j] > nums[idx-1]:
            j += 1
        j -= 1
        nums[idx-1], nums[j] = nums[j], nums[idx-1]
        nums[idx:] = nums[idx:][::-1]
        