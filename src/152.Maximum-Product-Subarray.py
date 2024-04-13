class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        min_so_far, max_so_far = 1, 1

        for num in nums:
            prod1 =  max_so_far * num
            prod2 = min_so_far * num
            max_so_far = max(prod1, prod2, num)
            min_so_far = min(prod1, prod2, num)
            res = max(res, max_so_far)
        
        return res