class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = [[-1] * len(s2) for _ in s1]
        
        # Answer for s1[i:] and s2[j:]
        def dp(s1, i, s2, j):
            if i == len(s1):
                return sum([ord(c) for c in s2[j:]])
            if j == len(s2):
                return sum([ord(c) for c in s1[i:]])
            if memo[i][j] != -1:
                return memo[i][j]
            if s1[i] == s2[j]:
                memo[i][j] = dp(s1, i+1, s2, j+1)
            else:
                memo[i][j] = min(dp(s1, i, s2, j+1) + ord(s2[j]),
                                 dp(s1, i+1, s2, j) + ord(s1[i]))
            return memo[i][j]
        
        return dp(s1, 0, s2, 0)