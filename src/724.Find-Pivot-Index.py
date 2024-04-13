class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # prefix_left[i] is the sum of nums[:i] (strictly to the left of index i)
        prefix_left = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_left[i] = prefix_left[i-1] + nums[i-1]
        
        total_sum = sum(nums)
        for i in range(n):
            if 2 * prefix_left[i] == total_sum - nums[i]:
                return i

        return -1