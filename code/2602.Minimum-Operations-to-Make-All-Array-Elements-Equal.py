class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        ans = [0] * m
        # it doesn't matter which order we mutate nums
        nums.sort()
        totalSum = sum(nums)
        prefixSum = [0] * (n + 1)
        for i in range(1, n+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]

        for idx in range(m):
            query = queries[idx]
            splitIdx = bisect.bisect_right(nums, query)
            # we need a sum of nums[:splitIdx]
            ans[idx] = (query * splitIdx -  prefixSum[splitIdx]) + (totalSum - prefixSum[splitIdx] - query * (n - splitIdx))

        return ans
