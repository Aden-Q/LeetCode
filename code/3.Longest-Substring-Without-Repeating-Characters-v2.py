from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 0
        window = Counter()
        left = 0
        right = left
        while right < len(s):
            window[s[right]] += 1
            while window[s[right]] >= 2:
                window[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length