class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        temp = (32 - len(n)) * '0' + n
        return int(temp[::-1], 2)