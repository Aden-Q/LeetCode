class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        
        for idx, c in enumerate(list(columnTitle)[::-1]):
            res += 26 ** idx * (ord(c) - ord('A') + 1)
        
        return res