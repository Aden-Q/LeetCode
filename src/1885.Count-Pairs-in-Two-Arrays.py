class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # conversion: (nums1[i] - nums2[i]) > - (nums1[j] - nums2[j])
        nums = [0] * len(nums1)
        nums = sorted([-(nums1[i] - nums2[i]) for i in range(len(nums1))])
        res = 0
        for i in range(len(nums1)):
            cur = nums1[i] - nums2[i]
            res += bisect.bisect_left(nums, nums1[i] - nums2[i])
            # if val is positve, -val is counted at the same index which is what we don't want
            if cur > 0:
                res -= 1
        # // 2 because every pair is counted twice
        return res // 2
