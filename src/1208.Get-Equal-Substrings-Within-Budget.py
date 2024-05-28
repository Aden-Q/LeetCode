class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # sliding window
        left = right = 0
        total_cost = 0
        while right < len(s):
            total_cost += abs(ord(s[right]) - ord(t[right]))
            if total_cost > maxCost:
                total_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            right += 1
        
        return right - left
