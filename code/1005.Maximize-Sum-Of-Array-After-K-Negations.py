class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        least_non_neg = float('inf')
        # negate all negative numbers in the first round
        # if less than k times, then negate the least non-negative number in the second round
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                # negate
                nums[i] = -nums[i]
                k -= 1
            # after negation, do the comparision
            if nums[i] < least_non_neg:
                least_non_neg = nums[i]
            res += nums[i]
        if k % 2 == 1:
            res -= 2 * least_non_neg
        return res