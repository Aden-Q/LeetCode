class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for c in s:
            if c not in counter.keys():
                counter[c] = 1
            else:
                counter[c] += 1
        for c in t:
            if c not in counter.keys():
                return False
            else:
                counter[c] -= 1
        for k, v in counter.items():
            if v != 0:
                return False
        return True