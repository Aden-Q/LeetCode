from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter1 = Counter(s)
        counter2 = Counter(t)
        key_set = set()
        
        for key in counter1.keys():
            key_set.add(key)
            
        for key in counter2.keys():
            key_set.add(key)
        
        res = 0
        # Append either to s or to t
        for key in key_set:
            res += abs(counter1[key] - counter2[key])
        
        return res