class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            abs_idx = abs(nums[idx])
            if nums[abs_idx] < 0:
                return abs_idx
            nums[abs_idx] *= -1
        