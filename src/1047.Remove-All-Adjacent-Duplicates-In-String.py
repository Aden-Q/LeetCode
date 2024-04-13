class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) == 0:
                res.append(c)
            elif res[-1] == c:
                res.pop()
            else:
                res.append(c)
                
        return "".join(res)