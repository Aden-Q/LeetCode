class Solution:
    def minimumDeletions(self, s: str) -> int:
        # the is a LIS problem
        n = len(s)
        stack = []
        for c in s:
            idx = bisect.bisect_right(stack, c)
            if idx == len(stack):
                stack.append(c)
            else:
                stack[idx] = c
        
        return len(s) - len(stack)
