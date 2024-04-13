class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        need_to_remove = set()
        # this stack only has '('
        stack = []
        for idx, c in enumerate(s):
            if c not in ['(', ')']:
                continue
            if c == '(':
                stack.append(idx)
            else:
                if stack:
                    stack.pop()
                else:
                    need_to_remove.add(idx)
        
        while stack:
            need_to_remove.add(stack.pop())

        ans = []
        for idx, c in enumerate(s):
            if idx not in need_to_remove:
                ans.append(c)

        return ''.join(ans)
