from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        for k in t:
            if counter1[k] != counter2[k]:
                return k