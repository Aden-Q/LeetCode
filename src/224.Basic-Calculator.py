class Solution:
    def calculate(self, s: str) -> int:
        # first we delete all space characters ' ' since they do not have any semantic meaning
        s = s.replace(' ', '')

        # evaluate an expression consisting of digits, +, and -
        # there can be multiple prefix of -
        def eval(s: str) -> int:
            if len(s) == 0:
                return 0
            # we use recursive call to eliminate '+-' sign
            sign = 1
            start = 0
            while s[start] in '+-':
                # read until there's no sign left
                if s[start] == '-':
                    sign *= -1
                start += 1

            # read the number
            length = 0
            while start + length < len(s) and s[start+length].isdigit():
                length += 1
                
            # now s[start:start+length] is the full number
            return sign * int(s[start:start+length]) + eval(s[start+length:])
        
        # the second thing is to get rid of all '(' and ')'
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx].isdigit():
                # if the current character is a digit, we read the full number
                length = 0
                while (idx + length) < len(s) and s[idx+length].isdigit():
                    length += 1
                
                # now s[idx:idx+length] is the full number
                stack.append(s[idx:idx+length])
                idx = idx + length
            elif s[idx] in '(+-':
                stack.append(s[idx])
                idx += 1
            elif s[idx] == ')':
                # we need to process a pair of '()'
                # so we pop until we see the first open bracket, and evaluate the string
                s_exp = ''
                while stack[-1] != '(':
                    s_exp = stack.pop() + s_exp
                # pop '('
                stack.pop()
                # evaluate the expression and push the result into the stack
                stack.append(str(eval(s_exp)))
                idx += 1

        # once exiting the while loop, we will have an expression without any '(' or ')'
        # so we can evaluate it and get the final result
        return eval(''.join(stack))
