class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        state = [False] * n 
        
        # the power of nums[:end+1]
        @cache
        def dp(end, k_remain) -> bool:
            if k_remain == 0:
                return int(pow(2, end+1)) % mod
            
            if k_remain < 0 or end < 0:
                return 0
            
            res = (2 * dp(end-1, k_remain) + dp(end-1, k_remain - nums[end])) % mod
            return int(res)
        
        return dp(n-1, k)
