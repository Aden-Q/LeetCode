class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in s]
        # dp[i][j] is true if s[i]...s[j] is a palindromic substring
        # is false elsewise
        max_len = 1
        res = s[0]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif j == i + 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                if dp[i][j] == True and j-i+1 > max_len:
                    max_len = j-i+1
                    res = s[i:j+1]
        return res        