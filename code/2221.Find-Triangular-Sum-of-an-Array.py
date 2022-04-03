class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        newNums = [0] * (len(nums) - 1)
        for i in range(len(nums) - 1):
            newNums[i] = (nums[i] + nums[i + 1]) % 10
        return self.triangularSum(newNums)