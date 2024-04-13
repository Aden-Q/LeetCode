class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n % 2 == 1:
            return n == 1
        return self.isPowerOfTwo(n // 2)
            