class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        # dp[i] has three status:
        # 1: GOOD, -1: BAD, 0: UNKNOWN
        # to indicate whether we can
        # reach the end starting from this position
        dp = [0] * length
        # Initial value, the last position must be a good position
        dp[-1] = 1
        
        for i in range(length - 2, -1, -1):
            # The rightmost position we can jump
            # starting from position i
            max_pos = min(length - 1, i + nums[i])
            for j in range(i + 1, max_pos + 1):
                if dp[j] == 1:
                    dp[i] = 1
                    break
                # else if dp[j] is BAD or UNKNOWN
                # dp[i] is also UNKOWN, so do not change
                # the status of dp[i] otherwise
                
        return dp[0]