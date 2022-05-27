class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        num_diff = 0
        diff_idx1 = -1
        diff_idx2 = -1
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                num_diff += 1
                if diff_idx1 < 0:
                    diff_idx1 = i
                else:
                    diff_idx2 = i
        if num_diff > 2:
            return False
        if (s1[diff_idx1], s1[diff_idx2]) == (s2[diff_idx2], s2[diff_idx1]):
            return True
        return False