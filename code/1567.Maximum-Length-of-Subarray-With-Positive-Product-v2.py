class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # p[i] represents the maximum length of subarray with positive product
        # including nums[i]
        p = 0
        # n[i] represents the maximum length of subarray with positive product
        # including nums[i]
        n = 0
        # Initialization
        if nums[0] > 0:
            p = 1
        elif nums[0] < 0:
            n = 1
        
        res = p
        # dp state transfer
        for i in range(1, len(nums)):
            if nums[i] == 0:
                p = 0
                n = 0
            elif nums[i] > 0:
                p = p + 1
                n = n + 1 if n else 0
            else:
                temp = n
                n = p + 1
                p = temp + 1 if temp else 0
            res = max(res, p)
            
        return res