class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2:
            return False
        for i in range(len(s)):
            if s[i:i+3] == 'LLL':
                return False
        return True