class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # LIS problem
        stack = []
        for c in s:
            idx = bisect.bisect_right(stack, c)
            if idx == len(stack):
                stack.append(c)
            else:
                stack[idx] = c
        
        return len(s) - len(stack)
