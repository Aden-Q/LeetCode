class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        max_len = 0

        # the maximum length of the subarray of nums1[:end1] and nums2[:end2]
        dp = [[0] * (n+1) for _ in range(m+1)]
        for row in range(1, m+1):
            for col in range(1, n+1):
                if nums1[row-1] == nums2[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                    max_len = max(max_len, dp[row][col])

        return max_len