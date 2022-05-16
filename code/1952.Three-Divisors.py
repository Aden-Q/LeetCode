class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        if int(sqrt(n)) ** 2 != n:
            return False
        for i in range(2, int(sqrt(n))):
            if n % i == 0:
                return False
        return True