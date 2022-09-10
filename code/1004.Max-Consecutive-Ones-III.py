class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # This problem can to converted to the following:
        # Find the longest subarray including at most k 0's
        left, right = 0, 0
        # We need to count the number of 1's in nums[left...right]
        # A prefix sum array can help we solve the problem
        # prefix_sum[i] is the summation of nums[0], nums[1], ..., nums[i]
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        def calSum(prefix_sum, i, j):
            if i > 0:
                return prefix_sum[j] - prefix_sum[i-1]
            return prefix_sum[j]
        
        max_len = 0
        while right < len(nums):
            right += 1
            
            # The current window is nums[left...right-1]
            while right - left - calSum(prefix_sum, left, right-1) > k:
                left += 1
            max_len = max(max_len, right - left)
        
        return max_len