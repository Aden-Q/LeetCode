class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        res = 0

        for key in c:
            res += c[key] // 2 * 2
        
        return res + 1 if res < len(s) else res
        