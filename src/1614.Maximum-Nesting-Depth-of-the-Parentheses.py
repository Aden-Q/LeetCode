class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        
        curr_depth = 0
        for c in s:
            if c == '(':
                curr_depth += 1
            if c == ')':
                curr_depth -= 1
            res = max(res, curr_depth)
        
        return res