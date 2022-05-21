from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed = Counter(s1)
        window = Counter()
        left = 0
        right = 0
        sz = len(s2)
        while right < sz:
            r_char = s2[right]
            right += 1
            window[r_char] += 1
            if needed[r_char] != 0 and needed == window:
                return True
            while window[r_char] > needed[r_char]:
                l_char = s2[left]
                left += 1
                window[l_char] -= 1
        return False
        