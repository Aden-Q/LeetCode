class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        minNum = nums[0]
        maxNum = nums[-1]
        res = maxNum - minNum
        
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i+1]
            res = min(res, max(maxNum - k, a + k) - min(minNum + k, b - k))
            
        return res