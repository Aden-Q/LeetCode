class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cntOnes = 0
        for c in s:
            if c == '1':
                cntOnes += 1

        return '1' * (cntOnes - 1) + '0' * (len(s) - cntOnes) + '1'
