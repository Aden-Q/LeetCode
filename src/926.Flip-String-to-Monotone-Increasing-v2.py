class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        num_ones_before = [0] * n
        cnt_ones = 0
        for i in range(n):
            num_ones_before[i] = cnt_ones
            if s[i] == '1':
                cnt_ones += 1
        
        # returns the minimum number of flips for the prefix string of s, up to index end
        def dp(end) -> int:
            if end == 0:
                return 0
            if s[end] == '1':
                return dp(end-1)
            
            return min(1 + dp(end-1), num_ones_before[end])

        return dp(n-1)
