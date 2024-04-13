class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s)
        start = 0
        intervals = []
        while start < len(s):
            for word in words:
                length = len(word)
                if s[start:start+length] == word:
                    intervals.append([start, start + length])
            start += 1

        for start, end in intervals:
            for i in range(start, end):
                bold[i] = True

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
