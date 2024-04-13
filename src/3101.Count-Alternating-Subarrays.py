class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total_alter_subarrays = 0
        
        def dp(end) -> int:
            nonlocal total_alter_subarrays
            if end == 0:
                total_alter_subarrays += 1
                return 1
            
            prev_alter = dp(end-1)
            ans = 1
            if nums[end] != nums[end-1]:
                ans += prev_alter
            
            total_alter_subarrays += ans
            return ans
        
        dp(n - 1)
        return total_alter_subarrays
