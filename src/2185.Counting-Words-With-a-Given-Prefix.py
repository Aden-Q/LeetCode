class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        
        for word in words:
            if word[:len(pref)] == pref:
                cnt += 1
        
        return cnt