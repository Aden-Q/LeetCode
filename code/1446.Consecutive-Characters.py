class Solution:
    def maxPower(self, s: str) -> int:
        start = 0
        count = 0
        max_count = 0
        right = start
        while right < len(s):
            if s[right] != s[start]:
                start = right
                count = 0
            right += 1
            count += 1
            max_count = max(max_count, count)
        return max_count