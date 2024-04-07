class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_left = []
        stack_star = []
        for idx, c in enumerate(s):
            if c == '(':
                stack_left.append(idx)
            elif c == ')':
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
            else:
                stack_star.append(idx)

        while stack_left and stack_star:
            if stack_star[-1] > stack_left[-1]:
                stack_left.pop()
            
            stack_star.pop()

        return not stack_left
