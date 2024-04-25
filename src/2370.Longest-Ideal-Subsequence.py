class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            c_offset = ord(c) - 97
            start = max(0, c_offset-k)
            end = min(25, c_offset+k)+1
            dp[c_offset] = max(dp[start:end]) + 1

        return max(dp)  
