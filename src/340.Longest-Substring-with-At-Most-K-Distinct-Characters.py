class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0, 0
        window = Counter()
        max_len = 0

        while right < len(s):
            window[s[right]] += 1
            if len(window) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
            right += 1

        return right - left