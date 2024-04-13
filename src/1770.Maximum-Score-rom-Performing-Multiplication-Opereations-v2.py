class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        @lru_cache
        def dp(left, idx) -> int:
            # right will be n - 1 - (idx - left)
            if idx == m:
                # no operations left
                return 0
            # left or right will never go beyond the boundary given the input that n >= m
            # so we don't need to worry about that edge case
            return max(nums[left] * multipliers[idx] + dp(left+1, idx+1), nums[n-1-(idx-left)] * multipliers[idx] + dp(left, idx+1))

        return dp(0, 0)