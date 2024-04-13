from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = Counter()
        res = 0
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            window[c] += 1
            right += 1
            while window[c] > 1:
                d = s[left]
                window[d] -= 1
                left += 1
            res = max(res, right - left)
        return res