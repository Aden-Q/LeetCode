class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1] * len(s) for _ in s]
        
        # represents the answer for s[i...j], inclusive
        def dp(s, i, j):
            # Base case: one character in the subsequence
            if i == j:
                return 1
            if i > j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if s[i] == s[j]:
                memo[i][j] = dp(s, i+1, j-1) + 2
            else:
                memo[i][j] = max(dp(s, i+1, j),
                                 dp(s, i, j-1))
            return memo[i][j]
        
        return dp(s, 0, len(s) - 1)