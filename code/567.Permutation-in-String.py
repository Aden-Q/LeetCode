from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        num_valid = 0
        need = Counter(s1)
        window = Counter()
        
        while right < len(s2):
            c = s2[right]
            right += 1
            window[c] += 1
            if window[c] == need[c]:
                num_valid += 1
            
            while num_valid == len(need):
                if right - left == len(s1):
                    return True
                d = s2[left]
                left += 1
                if window[d] == need[d]:
                    num_valid -= 1
                window[d] -= 1
        return False