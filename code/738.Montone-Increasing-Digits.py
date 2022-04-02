class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        n = str(n)
        for i in range(len(n) - 2, -1, -1):
            if n[i] > n[i+1]:
                return self.monotoneIncreasingDigits(int(n[:(i+1)]) - 1) * (10 ** (len(n) - i - 1)) + 10 ** (len(n) - i - 1) - 1
        return int(n)