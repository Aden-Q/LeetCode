class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx].isdigit():
                num = 0
                while idx < len(s) and s[idx].isdigit():
                    # read the full number
                    num = num * 10 + int(s[idx])
                    idx += 1
                stack.append(num)
            elif s[idx] in '+':
                # we need to delay the evaluation because there are possibly some * or / operations come later
                idx += 1
            elif s[idx] == '-':
                # read in the next number and make t negative
                num = 0
                idx += 1
                while idx < len(s) and s[idx].isdigit():
                    # read the full number
                    num = num * 10 + int(s[idx])
                    idx += 1
                stack.append(-num)
            elif s[idx] in '*/':
                # we need to read in the next operand and evaluate this operation
                num = stack.pop()
                next_num = 0
                is_mul = (s[idx] == '*')
                idx += 1
                while idx < len(s) and s[idx].isdigit():
                    # read the full number
                    next_num = next_num * 10 + int(s[idx])
                    idx += 1
                if is_mul:
                    stack.append(num * next_num)
                else:
                    stack.append(int(num / next_num))

        # now we have a stack consisting of only numbers, + and -, we evaluate it from left to right
        res = 0
        while stack:
            res += stack.pop()

        return res
