class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s_reversed = s[::-1]
        for i in range(len(s) - 1):
            if s_reversed.find(s[i:i+2]) >= 0:
                return True
        
        return False
