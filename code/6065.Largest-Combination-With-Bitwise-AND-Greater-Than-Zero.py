class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0] * 32

        for c in candidates:
            idx = 31
            while c > 0:
                if c & 1 == 1:
                    bits[idx] += 1
                c = c >> 1
                idx -= 1
                
        return max(bits)