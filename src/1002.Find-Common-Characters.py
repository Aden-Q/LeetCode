class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        candidates = words[0]
        words = [Counter(word) for word in words]
        for c in candidates:
            is_in_all = True
            for word in words:
                if word[c] <= 0:
                    is_in_all = False
                    break
                
                word[c] -= 1
            
            if is_in_all:
                res.append(c)
        
        return res
