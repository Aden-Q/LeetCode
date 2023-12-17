class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def evalOps(token, op1, op2):
            if token == '+':
                return op1 + op2
            elif token == '-':
                return op1 - op2
            elif token == '*':
                return op1 * op2
            elif token == '/':
                return int(op1 / op2)
        
        s = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                second, first = s.pop(), s.pop()
                # calculate the result
                res = evalOps(token, first, second)
                # push the result onto the operand stack
                s.append(res)
            else:
                # is an operator
                s.append(int(token))
        
        return s[0]