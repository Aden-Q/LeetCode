class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = Counter()
        prefix = ""
        res = 0

        for c in s:
            counter[c] += 1
            res += counter[c]

        return res
