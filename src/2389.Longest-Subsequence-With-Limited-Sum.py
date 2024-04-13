class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        ans = [0] * m
        nums.sort()
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        # greedy
        for i in range(m):
            ans[i] = bisect.bisect_right(prefixSum, queries[i]) - 1

        return ans
