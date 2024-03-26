class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            ans += bisect.bisect_left(nums, target - num, 0, i)
        
        return ans
