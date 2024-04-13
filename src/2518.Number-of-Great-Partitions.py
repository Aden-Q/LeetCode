class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        if total_sum < 2 * k:
            return 0

        mod = 10 ** 9 + 7
        n = len(nums)
        # the problem now is converted to: select num from nums, such that the total sum t satisfies:
        # t >= k
        # total_sum - t >= k
        # so we need total_sum - k >= t >= k

        # returns the number of ways to select from nums[start:] such that the total sum is less than k
        @cache
        def dp(start, upper) -> int:
            if upper <= 0:
                return 0
            if start == n:
                # nothing to select from, there's one way (select nothing)
                return 1

            # divide to sub problems:
            # 1. we do not choose nums[start]
            # 2. we choose nums[start]
            return (dp(start+1, upper) + dp(start+1, upper - nums[start])) % mod

        return (2 ** n - 2 * dp(0, k)) % mod
