class Solution:
    def countSubstrings(self, s: str) -> int:
        # expand around centers, we have len(s) centers to check in total
        cnt = 0

        # count odd length palindromes
        for idx in range(len(s)):
            width = 0
            while idx - width >= 0 and idx + width < len(s):
                if s[idx - width] == s[idx + width]:
                    cnt += 1
                    width += 1
                else:
                    break

        # count even length palindromes
        for idx in range(len(s) - 1):
            first, second = idx, idx + 1
            while first >= 0 and second < len(s) and s[first] == s[second]:
                cnt += 1
                first -= 1
                second += 1
        
        return cnt
