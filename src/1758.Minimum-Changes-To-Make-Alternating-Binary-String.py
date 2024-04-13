class Solution:
    def minOperations(self, s: str) -> int:
        flip = False
        # first pass checking the number of changes need to make it 0101...
        cnt1 = 0
        for c in s:
            if flip:
                if c != '0':
                    cnt1 += 1
            elif c != '1':
                cnt1 += 1
            flip = not flip

        flip = True
        cnt2 = 0
        for c in s:
            if flip:
                if c != '0':
                    cnt2 += 1
            elif c != '1':
                cnt2 += 1
            flip = not flip

        return min(cnt1, cnt2)