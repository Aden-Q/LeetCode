from collections import defaultdict
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ht = defaultdict(list)
        
        for i in range(26):
            ht[i].append(-1)
        for idx, c in enumerate(s):
            ht[ord(c) - ord('A')].append(idx)
        for i in range(26):
            ht[i].append(len(s))
        
        res = 0
        for c in ht.keys():
            for pivot in range(1, len(ht[c]) - 1):
                # 3-element tuple (ht[c][pivot-1], ht[c][pivot], ht[c][pivot+1])
                res += (ht[c][pivot] - ht[c][pivot-1]) * (ht[c][pivot+1] - ht[c][pivot])
        
        return res