from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        s_sorted = sorted(counter.keys(), key = lambda x:counter[x], reverse=True)
        res = ''
        for k in s_sorted:
            res += k * counter[k]
        
        return res