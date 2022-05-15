class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        start = words[0]
        res = []
        res.append(start)
        for word in words:
            if sorted(word) == sorted(start):
                continue
            start = word
            res.append(start)
        return res