from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        dc1 = Counter(s)
        dc2 = Counter(target)
        min_v = float('inf')
        for c in target:
            min_v = min(min_v, dc1[c] // dc2[c])
        return min_v
            