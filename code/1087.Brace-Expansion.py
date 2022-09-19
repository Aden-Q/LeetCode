class Solution:
    def expand(self, s: str) -> List[str]:
        # Assuming that there are no duplicates in each candidate list
        candidates = []
        
        idx = 0
        while idx < len(s):
            if s[idx] == '{':
                curr = []
                idx += 1
                while idx < len(s) and s[idx] != '}':
                    if s[idx] != ',':
                        curr.append(s[idx])
                    idx += 1
                if len(curr) != 0:
                    candidates.append(curr[:])
                idx += 1 # skip '}'
            else:
                candidates.append(s[idx])
                idx += 1
        
        # Build target strings with backtracking
        path = []
        res = []
        def backtrack(idx):
            nonlocal path, res
            if idx == len(candidates):
                res.append(''.join(path))
                return
            for c in candidates[idx]:
                path.append(c)
                backtrack(idx + 1)
                path.pop()
            
            return
        
        backtrack(0)
        res.sort()
        return res