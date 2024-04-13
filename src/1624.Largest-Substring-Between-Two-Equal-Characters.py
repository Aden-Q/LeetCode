class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ht = defaultdict(int)
        max_len = -1
        for idx, c in enumerate(s):
            if c in ht:
                max_len = max(max_len, idx - ht[c] - 1)
            else:
                ht[c] = idx

        return max_len