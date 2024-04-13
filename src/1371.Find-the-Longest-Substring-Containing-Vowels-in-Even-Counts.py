class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_shift = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4,
        }
        dp = [-1] + [len(s)] * 32
        res = 0
        mask = 0
        for i in range(len(s)):
            c = s[i]
            if c in vowel_shift:
                mask ^= 1 << vowel_shift[c]
            res = max(res, i - dp[mask])
            dp[mask] = min(dp[mask], i)

        return res
