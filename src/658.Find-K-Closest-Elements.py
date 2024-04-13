from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = deque(arr)
        while len(q) > k:
            if x - q[0] <= q[-1] - x:
                q.pop()
            else:
                q.popleft()
        return q