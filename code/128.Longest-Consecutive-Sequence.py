from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_ct = 1
        cur_ct = 1
        nums = list(set(nums))
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                # reset the counter
                cur_ct = 1
            else:
                cur_ct += 1
                max_ct = max(max_ct, cur_ct)
        
        return max_ct