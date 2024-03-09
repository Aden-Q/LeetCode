class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans = 0
        idx = 1
        while idx < len(word):
            if abs(ord(word[idx]) - ord(word[idx-1])) <= 1:
                ans += 1
                idx += 2
            else:
                idx += 1
        
        return ans
