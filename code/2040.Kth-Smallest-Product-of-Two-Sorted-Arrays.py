class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # return True if the number of products <= x is < k
        def feasible(x) -> bool:
            total = 0
            for num1 in nums1:
                if num1 > 0:
                    total += bisect.bisect_right(nums2, x // num1)
                elif num1 < 0:
                    total += len(nums2) - bisect.bisect_left(nums2, ceil(x / num1))
                elif x >= 0:
                    total += len(nums2)

                if total >= k:
                    return False
                
            return True

        candidates = [nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
        left, right = min(candidates), max(candidates) + 1
        while left < right:
            mid = (right - left) // 2 + left
            if feasible(mid):
                left = mid + 1
            else:
                right = mid
        
        return left
