from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        # A map used to maintaining a mapping between
        # a character and its largest index + 1
        mp = {}
        left = 0
        
        for right in range(len(s)):
            if s[right] in mp:
                # We have seen the same character previously
                left = max(left, mp[s[right]])
            # The current window is [left, right], inclusive
            res = max(res, right - left + 1)
            # Store its largest index + 1
            mp[s[right]] = right + 1
        
        return res