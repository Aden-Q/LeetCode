class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        res = 0

        flag = False
        for key in c:
            if c[key] % 2 == 0:
                res += c[key]
            elif flag:
                res += c[key] - 1
            else:
                res += c[key]
                flag = True
        
        return res
        