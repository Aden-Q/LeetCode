from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window_substring = ''
        min_length = float('inf')
        left, right = 0, 0
        window = Counter()
        need = Counter(t)
        num_valid = 0
        
        while right < len(s):
            # get the current character
            c = s[right]
            right += 1
            window[c] += 1
            if window[c] == need[c]:
                num_valid += 1
            # print(left, ' ', right, ' ', num_valid)
            # shrink the window by moving the left ptr
            while num_valid == len(need):
                if right - left < min_length:
                    min_window_substring = s[left:right]
                    min_length = right - left
                if window[s[left]] == need[s[left]]:
                    num_valid -= 1
                window[s[left]] -= 1
                left += 1
            
        return min_window_substring