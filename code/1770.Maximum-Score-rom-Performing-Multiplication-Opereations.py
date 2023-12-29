class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        # we need 3 states to describe the problem:
        # the boundary of the nums, indicating the start and the end of the array
        # the current number of operations
        # the dp function returns the maximum score we can obtain from such a state
        @cache
        def dp(start, end, idx) -> int:
            if idx >= m:
                # when we cannot perform any operations, the maximum score we can obtain is 0
                return 0
            if start == end:
                # we only have a single choice to make
                return multipliers[idx] * nums[start]
            
            # otherwise in the current step we can either choose nums[start] or nums[end]
            return max(nums[start] * multipliers[idx] + dp(start+1, end, idx+1), nums[end] * multipliers[idx] + dp(start, end-1, idx+1))

        return dp(0, n-1, 0)