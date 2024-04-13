import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        heapq.heapify(nums1)
        heapq.heapify(nums2)
        
        for _ in range((m + n) // 2):
            if len(nums1) == 0:
                last = heapq.heappop(nums2)
            elif len(nums2) == 0:
                last = heapq.heappop(nums1)
            elif nums1[0] < nums2[0]:
                last = heapq.heappop(nums1)
            else:
                last = heapq.heappop(nums2)
        
        if len(nums1) == 0:
            cur = nums2[0]
        elif len(nums2) == 0:
            cur = nums1[0]
        elif nums2[0] < nums1[0]:
            cur = nums2[0]
        else:
            cur = nums1[0]
        
        if (m + n) % 2 == 1:
            return cur
        return (last + cur) / 2