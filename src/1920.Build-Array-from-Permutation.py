class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = nums.copy()

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans
