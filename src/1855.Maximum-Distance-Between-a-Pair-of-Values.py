class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        right = n-1
        left = min(m-1, right)
        max_dist = 0
        while left >= 0:
            if nums1[left] <= nums2[right]:
                max_dist = max(max_dist, right - left)
                left -= 1
            else:
                right -= 1
                left = min(left, right)
        return max_dist
            