class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        bold = [False] * len(s)
        start = 0
        while start < len(s):
            for word in words:
                length = len(word)
                if s[start:start+length] == word:
                    for i in range(start, start + length):
                        bold[i] = True
            start += 1

        res = ''
        i = 0
        while i < len(s):
            if not bold[i]:
                res += s[i]
                i += 1
            else:
                res += '<b>'
                while i < len(s) and bold[i]:
                    res += s[i]
                    i += 1
                res += '</b>'

        return res
