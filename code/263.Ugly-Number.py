class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factor = 2
        while factor <= 5:
            if n % factor == 0:
                while n % factor == 0:
                    n = n // factor
            
            factor += 1
        
        return n <= 5
