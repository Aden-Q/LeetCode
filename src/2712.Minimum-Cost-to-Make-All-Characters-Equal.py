class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        idx = 1
        while idx < n:
            # find the first mismatch
            if s[idx] != s[idx-1]:
                # we have 2 choices
                ans += min(idx, n-idx)
            
            idx += 1

        return ans
