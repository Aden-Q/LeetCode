from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        # Trimming
        if k > len(s):
            return 0
        
        cnt = Counter()
        left, right = 0, 0
        res = 0
        
        # Perform sliding window
        while right < len(s):
            cnt[s[right]] += 1
            while cnt[s[right]] > 1:
                # Shrinking
                cnt[s[left]] -= 1
                left += 1
            # In this window there is only unique characters
            if right - left + 1 == k:
                res += 1
                cnt[s[left]] -= 1
                left += 1
            right += 1
        
        return res