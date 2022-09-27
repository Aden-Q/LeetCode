from collections import deque

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = deque()
        ptr1 = len(num1) - 1
        ptr2 = len(num2) - 1
        # Carry bit when doing sum
        carry = 0
        
        while ptr1 >= 0 or ptr2 >= 0 or carry > 0:
            val1 = int(num1[ptr1]) if ptr1 >= 0 else 0
            val2 = int(num2[ptr2]) if ptr2 >= 0 else 0
            currSum = val1 + val2 + carry
            res.appendleft('%d' % (currSum % 10))
            carry = currSum // 10
            ptr1 -= 1
            ptr2 -= 1
        
        return ''.join(res)