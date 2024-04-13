class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        path = []
        res = []
        n = len(s)
        
        def backtrack(pos):
            nonlocal path, res, n
            if pos == n:
                res.append(''.join(path))
                return
            c = s[pos]
            if c.isdigit():
                path.append(c)
                backtrack(pos+1)
                path.pop()
                return
            else:
                path.append(c.upper())
                backtrack(pos+1)
                path.pop()
                
                path.append(c.lower())
                backtrack(pos+1)
                path.pop()
            return
        
        backtrack(0)
        return res
                