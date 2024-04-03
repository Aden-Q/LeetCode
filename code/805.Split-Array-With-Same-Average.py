class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # the problem is equivalent to find a subsequence of the given sum
        total = sum(nums)
        n = len(nums)
        average = total / n

        # return true if possible to take a subsequence from nums[:end+1] such that:
        # the length of the subsequence is k and the sum is currSum
        @cache
        def dp(end, k, currSum) -> bool:
            if k < 0 or end < 0 or currSum < -1e-6:
                return False
            if k == 0 and abs(currSum) < 1e-6:
                return True

            # we have 2 choices: take the current element, or don't take it
            return dp(end-1, k, currSum) or dp(end-1, k-1, currSum-nums[end])

        for k in range(1, n):
            val = k * average
            if val - int(val) > 1e-6:
                continue
            if dp(n-1, k, k * average):
                return True
        
        return False
