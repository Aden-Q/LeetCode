class Solution:
    def maxScore(self, s: str) -> int:
        # left substring: s[:ptr]
        # right substring: s[ptr:]
        # max ptr = len(s)
        ptr = 0
        left_num_zeros = 0
        right_num_ones = sum(1 for c in s if c == '1')
        res = 0

        while ptr < len(s) - 1:
            # non empty substrings
            if s[ptr] == '0':
                left_num_zeros += 1
            else:
                right_num_ones -= 1
            res = max(res, right_num_ones + left_num_zeros)
            ptr += 1

        return res