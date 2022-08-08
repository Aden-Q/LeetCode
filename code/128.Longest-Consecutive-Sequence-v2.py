from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # Build a hash set supporting O(1) lookup
        nums = set(nums)
        max_ct = 1
        
        for num in nums:
            if num - 1 in nums:
                # skip this number because it is not the lower bound
                continue
            cur_ct = 1
            cur_num = num
            
            while cur_num + 1 in nums:
                cur_ct += 1
                cur_num += 1
                
            # update the response
            max_ct = max(max_ct, cur_ct)
        
        return max_ct