class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        from collections import deque
        sign = 1
        if num < 0:
            sign = -1
            num = -num
        res = deque()
        while num > 0:
            res.appendleft(str(num % 7))
            num = num // 7
        
        if sign > 0:
            return ''.join(res)
        else:
            return '-' + ''.join(res)