class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # first collect all the letters
        letters = [c for c in s if c.isalpha()]
        res = []
        for c in s:
            if c.isalpha():
                res.append(letters.pop())
            else:
                res.append(c)
        return ''.join(res)