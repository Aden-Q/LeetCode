class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        min_adj_diff = inf
        for i in range(1, len(nums)):
            min_adj_diff = min(min_adj_diff, nums[i] - nums[i-1])
        
        return min_adj_diff
