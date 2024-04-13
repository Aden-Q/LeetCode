class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        # we don't need to increase nums[0], but starting from nums[1], we may need to increase it
        curr = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            curr = max(curr+1, nums[i])
            if nums[i] != curr:
                ans += curr - nums[i]
        
        return ans
