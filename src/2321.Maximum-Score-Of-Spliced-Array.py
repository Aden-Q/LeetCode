class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1Sum = sum(nums1)
        nums2Sum = sum(nums2)
        globalMaxScore = max(nums1Sum, nums2Sum)

        # the maximum sum of nums1 and nums2 if the swap ends at index 'end' (inclusive)
        def dp(end) -> (int, int):
            nonlocal globalMaxScore
            if end < 0:
                # nothing is swapped
                return nums1Sum, nums2Sum

            prevMaxNums1, prevMaxNums2 = dp(end-1)
            # for the current end, we have 2 choices:
            # 1. appending to the previous slice
            # 2. ignore the previous slice and only take the current one
            # we take whichever greater
            currMaxNums1, currMaxNums2 =  max(prevMaxNums1, nums1Sum) + nums2[end] - nums1[end],  max(prevMaxNums2, nums2Sum) + nums1[end] - nums2[end]

            globalMaxScore = max(globalMaxScore, currMaxNums1, currMaxNums2)

            return currMaxNums1, currMaxNums2

        dp(n-1)
        return globalMaxScore
