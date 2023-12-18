class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return self.myPow(1.0/x, -n)

        # now we can safely assume n > 0
        res = 1
        while n:
            if n % 2 == 1:
                res *= x
                n -= 1
            else:
                x *= x
                n = n // 2
        
        return res
