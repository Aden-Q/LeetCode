class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        not_found = 0
        if len(s) == 0:
            return True
        
        for c in t:
            if c == s[not_found]:
                not_found += 1
                if not_found == len(s):
                    return True

        return False