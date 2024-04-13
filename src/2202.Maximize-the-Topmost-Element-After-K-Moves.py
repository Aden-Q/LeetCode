class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1 and (k & 1):
            return -1
            
        res = -1
        for i in range(min(n, k-1)):
            res = max(res, nums[i])

        if n > k:
            res = max(res, nums[k])

        return res
