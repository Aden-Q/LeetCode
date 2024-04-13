class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr_idx = 0
        while curr_idx < len(nums):
            # append the next 3 elements into the result list
            if curr_idx + 2 >= len(nums):
                # impossible
                return []
            if nums[curr_idx + 2] - nums[curr_idx] > k:
                # impossible
                return []
            # possible
            res.append([nums[curr_idx], nums[curr_idx+1], nums[curr_idx+2]])
            curr_idx += 3
        
        return res
