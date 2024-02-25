class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start = 0
        while start < len(nums):
            end = start
            while end < len(nums) and nums[end] == nums[start] + end - start:
                end += 1
            
            if end == start + 1:
                res.append(str(nums[start]))
            else:
                res.append(str(nums[start]) + '->' + str(nums[end - 1]))

            start = end
        
        return res
