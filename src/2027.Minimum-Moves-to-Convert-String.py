class Solution:
    def minimumMoves(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != 'X':
                i += 1
            if i < len(s):
                count += 1
                i += 3
        return count