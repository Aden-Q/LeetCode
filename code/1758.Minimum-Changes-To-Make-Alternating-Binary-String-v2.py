class Solution:
    def minOperations(self, s: str) -> int:
        flip = False
        # first pass checking the number of changes need to make it 0101...
        cnt1 = 0
        for c in s:
            if flip:
                if c != '0':
                    cnt1 += 1
            else:
                if c != '1':
                    cnt1 += 1

            flip = not flip

        return min(cnt1, len(s) - cnt1)