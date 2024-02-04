class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter()
        need = Counter(t)
        # the number of characters satisfied in the current window
        num_char = 0
        res = s + '0'

        # we will never shrink the window by a step > 1
        left, right = 0, 0
        while right < len(s):
            window[s[right]] += 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                num_char += 1
            # left
            while left <= right and window[s[left]] > need[s[left]]:
                window[s[left]] -= 1
                left += 1

            if num_char == len(need) and right - left + 1 < len(res):
                res = s[left:right+1]

            right += 1

        return res if res != s + '0' else ''
