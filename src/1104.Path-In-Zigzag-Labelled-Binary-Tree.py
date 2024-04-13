from collections import deque

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = deque()
        i = 0
        while 2 ** i <= label:
            i += 1
        while label != 0:
            res.appendleft(label)
            label = (2 ** (i-1) + 2 ** (i) - 1 - label) // 2
            i -= 1
            
        return res