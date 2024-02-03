class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x:
            remainder = x % 10
            res = res * 10 + remainder
            x = x // 10
        
        res *= sign
        if res > 2 ** 31 - 1 or res < - 2 ** 31:
            return 0

        return res
