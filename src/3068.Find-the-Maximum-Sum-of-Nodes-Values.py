class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        ans = 0
        flip_count_odd = False
        min_cost = inf
        for num in nums:
            num_xor = num ^ k
            ans += max(num_xor, num)
            if num_xor > num:
                flip_count_odd = not flip_count_odd
                # the minimal cost if flip back
            min_cost = min(min_cost, abs(num - num_xor))

        if flip_count_odd:
            # we did one more flip, we need to revert the one that gives us the least gain
            ans -= min_cost

        return ans
