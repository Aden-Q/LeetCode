class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        counter = collections.defaultdict(int)
        for c in ransomNote:
            counter[c] += 1
        for c in magazine:
            counter[c] -= 1
        for v in counter.values():
            if v > 0:
                return False
        return True