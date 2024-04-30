class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bitmask = 0
        counter = Counter()
        counter[0] = 1
        res = 0
        
        for c in word:
            offset = ord(c) - 97
            bitmask ^= (1 << offset)
            res += counter[bitmask]

            for offset in range(10):
                bitmask_diff = bitmask ^ (1 << offset)
                res += counter[bitmask_diff]
            
            counter[bitmask] += 1
        return res
