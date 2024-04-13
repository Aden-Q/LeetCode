class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for word in s.split():
            res.append(word[::-1])
        return ' '.join(res)