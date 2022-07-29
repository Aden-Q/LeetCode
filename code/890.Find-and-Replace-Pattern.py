class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        for word in words:
            ht1 = {}
            ht2 = {}
            flag = True
            for w, p in zip(word, pattern):
                if w not in ht1:
                    ht1[w] = p
                if p not in ht2:
                    ht2[p] = w
                if (w, p) != (ht2[p], ht1[w]):
                    flag = False
                    break
            if flag:
                res.append(word)
        
        return res