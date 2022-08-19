class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums)):
            cur_max, cur_min = nums[i], nums[i]
            for j in range(i+1, len(nums)):
                cur_max = max(cur_max, nums[j])
                cur_min = min(cur_min, nums[j])
                res += cur_max - cur_min
                
        return res 