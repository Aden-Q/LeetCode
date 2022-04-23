from collections import deque

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A = deque(sorted(nums1))
        B = deque(sorted([(val, idx) for idx, val in enumerate(nums2)]))
        res = [0] * len(nums2)
        while len(B) > 0:
            val, idx = B.pop()
            if A[-1] > val:
                res[idx] = A.pop()
            else:
                res[idx] = A.popleft()
        return res  