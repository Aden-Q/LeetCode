class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # O(1) space, O(NlogN) time solution
        res = []
        nums.sort()
        idx = 0
        while idx < len(nums):
            curr_num = nums[idx]
            cnt = 0
            while idx < len(nums) and nums[idx] == curr_num:
                cnt += 1 
                idx += 1
            
            if cnt > len(nums) // 3:
                res.append(curr_num)

        return res
