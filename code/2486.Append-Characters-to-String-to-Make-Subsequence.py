class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        index_t = 0
        index_s = 0
        # try to find the longest prefix in t such that there's a subsequence of it in s
        while index_t < len(t) and index_s < len(s):
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            else:
                index_s += 1

        return len(t) - index_t
