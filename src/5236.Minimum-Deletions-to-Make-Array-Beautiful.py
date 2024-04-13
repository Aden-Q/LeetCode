class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        count = 0
        i = 0
        while i < len(nums) - 1:
            while i < len(nums) - 1 and i % 2 == 0 and nums[i+1] == nums[i]:
                nums.pop(i+1)
                count += 1
            i += 1
        if len(nums) % 2 == 0:
            return count
        else:
            return count + 1