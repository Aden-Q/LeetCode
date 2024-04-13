class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        s_idx = 0
        if len(s) != len(words):
            return False

        while s_idx < len(s):
            if s[s_idx] != words[s_idx][0]:
                return False
            s_idx += 1
        
        return True
