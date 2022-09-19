class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0, 0
        counter = collections.Counter()
        res = 0
        
        while right < len(s):
            counter[s[right]] += 1
            right += 1
            while len(counter) > 2:
                # Shrink the window size
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            # Current window: [left, right)
            res = max(res, right - left)
            
        return res